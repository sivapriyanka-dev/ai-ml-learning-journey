from typing import TypedDict, Union
from langgraph.graph import StateGraph


class State(TypedDict):
    question: str
    calculation: Union[int, float]
    answer: str
    tool_used: str


def calculator_node(state):

    expression = (
        state["question"]
        .replace("What is", "")
        .replace("?", "")
        .strip()
    )

    result = eval(expression)

    print("Calculator Node:", result)

    return {
        "calculation": result,
        "tool_used": "calculator"
    }


def answer_node(state):

    answer = (
        f"The answer is "
        f"{state['calculation']}"
    )

    print("Answer Node:", answer)

    return {
        "answer": answer
    }


graph = StateGraph(State)

graph.add_node(
    "calculator",
    calculator_node
)

graph.add_node(
    "answer",
    answer_node
)

graph.set_entry_point(
    "calculator"
)

graph.add_edge(
    "calculator",
    "answer"
)

graph.set_finish_point(
    "answer"
)

app = graph.compile()

result = app.invoke(
    {
        "question":
        "What is 25 * 16?"
    }
)

print("\nFinal State:")
print(result)
print("\nAnswer only:")
print(result["answer"])

result = app.invoke(
    {
        "question":
        "What is 100 + 50?"
    }
)

print("\nFinal State:")
print(result)

result = app.invoke(
    {
        "question":
        "What is 90 / 3?"
    }
)

print("\nFinal State:")
print(result)
