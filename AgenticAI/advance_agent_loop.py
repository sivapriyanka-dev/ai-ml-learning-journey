from typing import TypedDict


# ==========================
# TOOLS
# ==========================

def calculator(expression):
    return eval(expression)


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
    thoughts: list
    observations: list


# ==========================
# AGENT
# ==========================

def agent(question):

    state = {
        "question": question,
        "thoughts": [],
        "observations": []
    }

    print("\n" + "=" * 50)
    print("Question:", question)

    # --------------------------------
    # SQUARE
    # --------------------------------

    if "square" in question.lower():

        thought = "Need to calculate 25 * 16"
        state["thoughts"].append(thought)

        print("\nThought:")
        print(thought)

        first_result = tools["calculator"](
            "25*16"
        )

        state["observations"].append(
            first_result
        )

        print("\nObservation:")
        print(first_result)

        thought = "Need square of result"
        state["thoughts"].append(thought)

        print("\nThought:")
        print(thought)

        second_result = tools["calculator"](
            f"{first_result}*{first_result}"
        )

        state["observations"].append(
            second_result
        )

        print("\nObservation:")
        print(second_result)

        print("\nFinal Answer:")
        print(second_result)

        print("\nState:")
        print(state)

        return second_result

    # --------------------------------
    # CUBE
    # --------------------------------

    elif "cube" in question.lower():

        thought = "Need to calculate 10 * 5"
        state["thoughts"].append(thought)

        print("\nThought:")
        print(thought)

        first_result = tools["calculator"](
            "10*5"
        )

        state["observations"].append(
            first_result
        )

        print("\nObservation:")
        print(first_result)

        thought = "Need cube of result"
        state["thoughts"].append(thought)

        print("\nThought:")
        print(thought)

        second_result = tools["calculator"](
            f"{first_result}*{first_result}*{first_result}"
        )

        state["observations"].append(
            second_result
        )

        print("\nObservation:")
        print(second_result)

        print("\nFinal Answer:")
        print(second_result)

        print("\nState:")
        print(state)

        return second_result

    # --------------------------------
    # SEARCH + CALCULATION
    # --------------------------------

    elif "python" in question.lower():

        thought = "Need information about Python"
        state["thoughts"].append(thought)

        print("\nThought:")
        print(thought)

        search_result = tools["search"](
            "python"
        )

        state["observations"].append(
            search_result
        )

        print("\nObservation:")
        print(search_result)

        thought = "Need calculation 20 * 5"
        state["thoughts"].append(thought)

        print("\nThought:")
        print(thought)

        calc_result = tools["calculator"](
            "20*5"
        )

        state["observations"].append(
            calc_result
        )

        print("\nObservation:")
        print(calc_result)

        final_answer = (
            f"{search_result}\n"
            f"Calculation Result: {calc_result}"
        )

        print("\nFinal Answer:")
        print(final_answer)

        print("\nState:")
        print(state)

        return final_answer

    else:

        print("\nNo matching workflow found.")

        return "I don't understand."


# ==========================
# TESTS
# ==========================

agent(
    "What is the square of 25 * 16?"
)

agent(
    "What is the cube of 10 * 5?"
)

agent(
    "Tell me about Python and calculate 20 * 5"
)
