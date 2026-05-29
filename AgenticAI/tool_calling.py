def calculator(expression):
    return eval(expression)


def knowledge_tool(question):
    knowledge = {
        "what is ai": "Artificial Intelligence is the simulation of human intelligence by machines.",
        "what is ml": "Machine Learning is a subset of AI."
    }

    return knowledge.get(question.lower().replace("?", ""), "I don't know.")


def agent(question):
    question_lower = question.lower()

    if any(op in question_lower for op in ["+", "-", "*", "/"]):
        expression = (
            question_lower
            .replace("what is", "")
            .replace("?", "")
            .strip()
        )

        result = calculator(expression)

        return f"Tool Used: Calculator\nAnswer: {result}"

    else:
        result = knowledge_tool(question)

        return f"Tool Used: Knowledge Tool\nAnswer: {result}"


question1 = "What is 25 * 16?"
question2 = "What is AI?"
question3 = "What is 25 + 16?"
question4 = "What is ML?"
question5 = "What is 90 / 3?"

print(agent(question1))
print()
print(agent(question2))
print()
print(agent(question3))
print()
print(agent(question4))
print()
print(agent(question5))
