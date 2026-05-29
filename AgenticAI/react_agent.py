import ollama


def calculator(expression):
    return str(eval(expression))


def current_year():
    return "2026"


def search(query):

    data = {
        "python":
        "Python is a programming language.",

        "agentic ai":
        "Agentic AI uses tools and reasoning."
    }

    return data.get(
        query.lower(),
        "No result found."
    )


def react_agent(question):

    print(f"\nQuestion: {question}")

    prompt = f"""
    You are a ReAct AI Agent.

    Available Tool:
    calculator(expression)
    year()
    search(query)

    If calculation is needed,
    respond ONLY:

    TOOL:calculator:<expression>

    If user asks current year respond ONLY:
    
    TOOL:year
    
    If information lookup is needed, respond ONLY:

    TOOL:search:<query>

    Question:
    {question}
    """

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    thought = response["message"]["content"]

    print("\nThought:")
    print(thought)

    if thought.startswith("TOOL:calculator:"):

        expression = thought.replace(
            "TOOL:calculator:",
            ""
        )

        print("\nAction:")
        print(expression)

        result = calculator(expression)

        print("\nObservation:")
        print(result)

        return f"\nFinal Answer: {result}"

    if thought == "TOOL:year":
        return current_year()
    if thought.startswith("TOOL:search:"):

        query = thought.replace(
            "TOOL:search:",
            ""
        )

        result = search(query)

        return f"\nFinal Answer: {result}"
    return thought


print(
    react_agent("What is 25 * 16?")
)

print()

print(
    react_agent("What year is it?")
)

print()

print(
    react_agent("What is Python?")
)
