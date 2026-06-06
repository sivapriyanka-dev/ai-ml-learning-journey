from typing import TypedDict
from langgraph.graph import StateGraph


# ======================
# TOOLS
# ======================

def calculator(expression):
    return str(eval(expression))


def search(query):

    knowledge = {
        "python": "Python is a programming language.",
        "react": "React is a frontend library.",
        "langgraph": "LangGraph is a framework for building AI agents."
    }

    return knowledge.get(
        query.lower(),
        "No result found."
    )


def year():
    return "2026"


def weather():
    return "30°C Sunny"


# ======================
# TOOL REGISTRY
# ======================

tools = {
    "calculator": calculator,
    "search": search,
    "year": year,
    "weather": weather
}


# ======================
# STATE
# ======================

class State(TypedDict):
    question: str
    tool_name: str
    tool_input: str
    tool_result: str


# ======================
# ROUTER NODE
# ======================

def router_node(state):

    question = state["question"].lower()

    # Calculator
    if any(op in question for op in ["+", "-", "*", "/"]):

        expression = (
            question
            .replace("what is", "")
            .replace("?", "")
            .strip()
        )

        return {
            "tool_name": "calculator",
            "tool_input": expression
        }

    # Search - Python
    elif "python" in question:

        return {
            "tool_name": "search",
            "tool_input": "python"
        }

    # Search - React
    elif "react" in question:

        return {
            "tool_name": "search",
            "tool_input": "react"
        }

    # Search - LangGraph
    elif "langgraph" in question:

        return {
            "tool_name": "search",
            "tool_input": "langgraph"
        }

    # Year
    elif "year" in question:

        return {
            "tool_name": "year",
            "tool_input": ""
        }

    # Weather
    elif "weather" in question:

        return {
            "tool_name": "weather",
            "tool_input": ""
        }

    return {
        "tool_name": "",
        "tool_input": ""
    }


# ======================
# TOOL EXECUTOR NODE
# ======================

def tool_executor_node(state):

    tool_name = state["tool_name"]

    if tool_name == "":

        return {
            "tool_result": "No tool selected."
        }

    tool = tools[tool_name]

    if tool_name in ["year", "weather"]:

        result = tool()

    else:

        result = tool(
            state["tool_input"]
        )

    return {
        "tool_result": result
    }


# ======================
# GRAPH
# ======================

graph = StateGraph(State)

graph.add_node(
    "router",
    router_node
)

graph.add_node(
    "tool_executor",
    tool_executor_node
)

graph.set_entry_point(
    "router"
)

graph.add_edge(
    "router",
    "tool_executor"
)

graph.set_finish_point(
    "tool_executor"
)

app = graph.compile()


# ======================
# TESTS
# ======================

questions = [
    "What is 25 * 16?",
    "Tell me about Python",
    "Tell me about React",
    "Tell me about LangGraph",
    "What year is it?",
    "What is the weather today?"
]

for question in questions:

    print("\n" + "=" * 50)

    result = app.invoke(
        {
            "question": question
        }
    )

    print("Question:", question)
    print("Tool Used:", result["tool_name"])
    print("Result:", result["tool_result"])
