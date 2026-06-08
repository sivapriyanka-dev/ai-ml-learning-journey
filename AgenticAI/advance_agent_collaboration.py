import ollama


# ==========================
# RESEARCH AGENT
# ==========================

def research_agent(topic):

    prompt = f"""
    Give 5 important points about:

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

def writer_agent(research_notes):

    prompt = f"""
    Write a short article using
    the following research:

    {research_notes}
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

def reviewer_agent(article):

    prompt = f"""
    Review this article.

    Provide:
    1. Strengths
    2. Improvements

    Article:

    {article}
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
# COLLABORATION WORKFLOW
# ==========================

def ai_team(topic):

    print("\n" + "=" * 60)

    print("\nSTEP 1 - RESEARCH AGENT")

    research = research_agent(topic)

    print(research)

    print("\nSTEP 2 - WRITER AGENT")

    article = writer_agent(research)

    print(article)

    print("\nSTEP 3 - REVIEWER AGENT")

    review = reviewer_agent(article)

    print(review)

    return {
        "research": research,
        "article": article,
        "review": review
    }


# ==========================
# TEST
# ==========================

result = ai_team(
    "Agentic AI"
)

print("\n" + "=" * 60)
print("\nFINAL OUTPUT")
print(result)
