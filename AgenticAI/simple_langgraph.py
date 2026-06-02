from typing import TypedDict
from langgraph.graph import StateGraph


class State(TypedDict):
    message: str


def node_a(state):
    print("Node A Executed")

    return {
        "message": state["message"] + " -> A"
    }


def node_b(state):
    print("Node B Executed")

    return {
        "message": state["message"] + " -> B"
    }


def node_c(state):
    print("Node C Executed")

    return {
        "message":
        state["message"] + " -> C"
    }


graph = StateGraph(State)

graph.add_node("node_a", node_a)
graph.add_node("node_b", node_b)
graph.add_node("node_c", node_c)

graph.set_entry_point("node_a")

graph.add_edge(
    "node_a",
    "node_b"
)

graph.add_edge(
    "node_b",
    "node_c"
)

graph.set_finish_point("node_c")

app = graph.compile()

result = app.invoke(
    {
        "message": "Start"
    }
)

print(result)
