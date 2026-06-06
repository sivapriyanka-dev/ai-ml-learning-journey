# Step 1: Simple Ollama Node
from langgraph.graph import StateGraph
from typing import TypedDict
import ollama


# def llm_node(question):

#     response = ollama.chat(
#         model="llama3",
#         messages=[
#             {
#                 "role": "user",
#                 "content": question
#             }
#         ]
#     )

#     return response["message"]["content"]


# print(
#     llm_node(
#         "What is Machine Learning?"
#     )
# )

# Step 2: Convert to LangGraph Node

class State(TypedDict):
    question: str
    answer: str


def llm_node(state):

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": state["question"]
            }
        ]
    )

    return {
        "answer":
        response["message"]["content"]
    }


graph = StateGraph(State)

graph.add_node(
    "llm",
    llm_node
)

graph.set_entry_point("llm")

graph.set_finish_point("llm")

app = graph.compile()

result1 = app.invoke(
    {
        "question": "Explain Machine Learning in 2 lines."
    }
)

result2 = app.invoke(
    {
        "question": "What is React?"
    }
)

print(result1["answer"])
print(result2)
