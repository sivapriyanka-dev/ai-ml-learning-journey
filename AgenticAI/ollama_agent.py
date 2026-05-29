import ollama
import re


def calculator(expression):
    try:
        return str(eval(expression))
    except Exception:
        return "Invalid expression"


def current_year():
    return "2026"


def agent(question):

    prompt = f"""
You are a tool-calling AI.

Rules:
- For math questions output ONLY:
TOOL:calculator:<expression>

- For year questions output ONLY:
TOOL:year

- Otherwise answer normally.

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

    answer = response["message"]["content"].strip()

    match = re.search(
        r"TOOL:calculator:(.*)",
        answer
    )

    if match:
        expression = match.group(1).strip()
        result = calculator(expression)

        return f"Tool Used: Calculator\nAnswer: {result}"

    if answer == "TOOL:year":
        return current_year()

    return answer


print(
    agent("What is 25 * 16?")
)

print()

print(
    agent("What is Artificial Intelligence?")
)

print()

print(
    agent("What year is it?")
)
