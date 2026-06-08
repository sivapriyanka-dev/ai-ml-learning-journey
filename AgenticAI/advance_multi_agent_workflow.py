import ollama


# ==========================
# PLANNER AGENT
# ==========================

def planner_agent(topic):

    prompt = f"""
    Create a plan to write a report about:

    {topic}

    Give only 3-5 steps.
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

    return response["message"]["content"]


# ==========================
# RESEARCH AGENT
# ==========================

def research_agent(topic):

    prompt = f"""
    Give important research points about:

    {topic}
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

    return response["message"]["content"]


# ==========================
# WRITER AGENT
# ==========================

def writer_agent(research):

    prompt = f"""
    Write a short report using:

    {research}
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

    return response["message"]["content"]


# ==========================
# REVIEWER AGENT
# ==========================

def reviewer_agent(report):

    prompt = f"""
    Review this report.

    Give:

    1. Strengths
    2. Improvements

    Report:

    {report}
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

    return response["message"]["content"]


# ==========================
# SUPERVISOR
# ==========================

def supervisor(topic):

    print("\n" + "=" * 70)

    print("\nSTEP 1: PLANNER AGENT")

    plan = planner_agent(topic)

    print(plan)

    print("\nSTEP 2: RESEARCH AGENT")

    research = research_agent(topic)

    print(research)

    print("\nSTEP 3: WRITER AGENT")

    report = writer_agent(research)

    print(report)

    print("\nSTEP 4: REVIEWER AGENT")

    review = reviewer_agent(report)

    print(review)

    return {
        "topic": topic,
        "plan": plan,
        "research": research,
        "report": report,
        "review": review
    }


# ==========================
# TEST
# ==========================

result = supervisor(
    "Agentic AI"
)

print("\n" + "=" * 70)
print("\nFINAL RESULT")
print(result)
