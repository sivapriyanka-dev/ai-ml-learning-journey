from typing import TypedDict
from langgraph.graph import StateGraph


class State(TypedDict):
    question: str
    answer: str


def router(state):
    question = state["question"]

    if any(op in question for op in ["+", "-", "*", "/"]):
        return "calculator"

    return "knowledge"


def calculator_node(state):
    question = state["question"]

    expression = (
        question.replace("What is", "")
        .replace("?", "")
        .strip()
    )

    result = eval(expression)

    return {
        "answer": str(result)
    }


knowledge = {
    "python": "Python is a programming language.",
    "react": "React is a frontend library.",
    "langgraph": "LangGraph is an AI agent framework."
}


def knowledge_node(state):
    question = state["question"].lower()

    for key, value in knowledge.items():
        if key in question:
            return {
                "answer": value
            }

    return {
        "answer": "I don't know."
    }


graph = StateGraph(State)

graph.add_node(
    "calculator",
    calculator_node
)

graph.add_node(
    "knowledge",
    knowledge_node
)

graph.set_conditional_entry_point(
    router
)

graph.set_finish_point("calculator")
graph.set_finish_point("knowledge")

app = graph.compile()

result = app.invoke(
    {
        "question": "What is 25 * 16?"
    }
)

print(result)

result = app.invoke(
    {
        "question": "What is Python?"
    }
)
print(result)

result = app.invoke(
    {
        "question": "Tell me about React"
    }
)

print(result)
