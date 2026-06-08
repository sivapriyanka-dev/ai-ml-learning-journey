from typing import TypedDict
from langgraph.graph import StateGraph
import ollama


# ==========================
# TOOLS
# ==========================

def calculator(expression):
    return str(eval(expression))


def search(query):

    knowledge = {
        "python": "Python is a programming language.",
        "react": "React is a frontend library.",
        "langgraph": "LangGraph is used for building AI agents."
    }

    return knowledge.get(
        query.lower(),
        "No information found."
    )


# ==========================
# TOOL REGISTRY
# ==========================

tools = {
    "calculator": calculator,
    "search": search
}


# ==========================
# STATE
# ==========================

class State(TypedDict):
    question: str
    tool_name: str
    tool_input: str
    tool_result: str
    answer: str


# ==========================
# LLM NODE
# ==========================

def llm_node(state):

    question = state["question"]

    prompt = f"""
You are an AI Agent.

Available tools:

1. calculator
2. search

Rules:

If math is needed:

Respond ONLY:

TOOL:calculator:<expression>

Example:
TOOL:calculator:25*16

If user asks about Python, React, LangGraph:

Respond ONLY:

TOOL:search:<keyword>

Example:
TOOL:search:python

Question:
{question}
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    output = response["message"]["content"]

    print("\nLLM Output:")
    print(output)

    if output.startswith("TOOL:calculator:"):

        expression = output.replace(
            "TOOL:calculator:",
            ""
        )

        return {
            "tool_name": "calculator",
            "tool_input": expression
        }

    elif output.startswith("TOOL:search:"):

        keyword = output.replace(
            "TOOL:search:",
            ""
        )

        return {
            "tool_name": "search",
            "tool_input": keyword
        }

    return {
        "answer": output
    }


# ==========================
# TOOL EXECUTOR NODE
# ==========================

def tool_executor_node(state):

    tool_name = state["tool_name"]

    tool = tools[tool_name]

    result = tool(
        state["tool_input"]
    )

    return {
        "tool_result": result
    }


# ==========================
# FINAL ANSWER NODE
# ==========================

def answer_node(state):

    return {
        "answer":
        f"Tool Result: {state['tool_result']}"
    }


# ==========================
# GRAPH
# ==========================

graph = StateGraph(State)

graph.add_node(
    "llm",
    llm_node
)

graph.add_node(
    "tool_executor",
    tool_executor_node
)

graph.add_node(
    "answer",
    answer_node
)

graph.set_entry_point(
    "llm"
)

graph.add_edge(
    "llm",
    "tool_executor"
)

graph.add_edge(
    "tool_executor",
    "answer"
)

graph.set_finish_point(
    "answer"
)

app = graph.compile()


# ==========================
# TESTS
# ==========================

questions = [
    "What is 25 * 16?",
    "Tell me about Python",
    "Tell me about React",
    "What is 100 + 50?"
]

for question in questions:

    print("\n" + "=" * 60)

    result = app.invoke(
        {
            "question": question
        }
    )

    print("\nQuestion:")
    print(question)

    print("\nFinal Answer:")
    print(result["answer"])
