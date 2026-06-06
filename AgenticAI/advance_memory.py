from typing import TypedDict


class State(TypedDict):
    messages: list[str]


def agent(state, question):

    state["messages"].append(
        f"User: {question}"
    )
    # Name question
    if "what is my name" in question.lower():

        for msg in state["messages"]:

            if "my name is" in msg.lower():

                name = msg.split("is")[-1].strip()

                answer = f"Your name is {name}"

                state["messages"].append(
                    f"Assistant: {answer}"
                )

                return answer

    # Location question
    if "where do i live" in question.lower():

        for msg in state["messages"]:

            if "i live in" in msg.lower():

                location = msg.split("in")[-1].strip()

                answer = f"Your location is {location}"

                state["messages"].append(
                    f"Assistant: {answer}"
                )

                return answer

    answer = "I don't know."

    state["messages"].append(
        f"Assistant: {answer}"
    )

    return answer


state = {
    "messages": [
        "User: My name is Priyanka",
        "User: I live in AI"
    ]
}

print(
    agent(
        state,
        "What is my name?"
    )
)

print(
    agent(
        state,
        "User: Where do I live?"
    )
)
