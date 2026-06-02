from typing import TypedDict
from langgraph.graph import StateGraph
from datetime import datetime


class State(TypedDict):
    question: str
    answer: str


def router(state):

    question = state["question"].lower()

    if any(op in question for op in ["+", "-", "*", "/"]):
        return "calculator"
    if "year" in question:
        return "year"
    return "search"


def calculator_node(state):

    expression = (
        state["question"]
        .replace("What is", "")
        .replace("?", "")
        .strip()
    )

    result = eval(expression)

    return {
        "answer": f"Math Answer: {result}"
    }


def year_node(state):
    return {
        "answer": str(datetime.now().year)
    }


def search_node(state):

    question = state["question"].lower()

    knowledge = {
        "python": "Python is a programming language.",
        "react": "React is a frontend library."
    }

    result = "No result found."

    for key in knowledge:
        if key in question:
            result = knowledge[key]

    return {
        "answer": result
    }


graph = StateGraph(State)

graph.add_node("calculator", calculator_node)
graph.add_node("search", search_node)
graph.add_node("year", year_node)

graph.set_conditional_entry_point(router)

graph.set_finish_point("calculator")
graph.set_finish_point("search")
graph.set_finish_point("year")

app = graph.compile()

print(
    app.invoke(
        {"question": "What is 50 * 20?"}
    )
)

print()

print(
    app.invoke(
        {"question": "Tell me about Python"}
    )
)

print()

print(
    app.invoke(
        {"question": "What year is it?"}
    )
)
