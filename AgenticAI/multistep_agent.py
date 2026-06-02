def calculator(expression):
    return eval(expression)


def search(query):
    data = {
        "python": "Python is a programming language.",
        "react": "React is a frontend library."
    }

    return data.get(query.lower())


def agent(question):

    if "square" in question.lower():

        print("Step 1: Calculate 25 * 16")

        first_result = calculator("25*16")

        print("Observation:", first_result)

        print("\nStep 2: Square the result")

        second_result = calculator(
            f"{first_result}*{first_result}"
        )

        print("Observation:", second_result)

        return second_result

    if "cube" in question.lower():

        print("Step 1: Calculate 10 * 5")

        first_result = calculator("10*5")

        print("Observation:", first_result)

        print("\nStep 2: Cube the result")

        second_result = calculator(
            f"{first_result}*{first_result}*{first_result}"
        )

        print("Observation:", second_result)

        return second_result

    if "python" in question.lower():

        result = search("python")

        print("Tool Used: Search")
        print("Observation:", result)

        return result

    return "I don't understand the question."


print(agent("What is the square of (25 * 16)?"))
print()
print(agent("What is the cube of (10 * 5)?"))
print()
print(agent("Tell me about Python and calculate 20 * 5"))
