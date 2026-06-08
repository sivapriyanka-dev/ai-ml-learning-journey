import ollama


# ======================
# RESEARCH AGENT
# ======================

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


# ======================
# WRITER AGENT
# ======================

def writer_agent(research):

    prompt = f"""
    Convert these notes into
    a short article:

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


# ======================
# REVIEWER AGENT
# ======================

def reviewer_agent(article):

    prompt = f"""
    Review this article.

    Suggest improvements.

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


# ======================
# MAIN WORKFLOW
# ======================

topic = "Agentic AI"

print("\nRESEARCH AGENT")
research = research_agent(topic)
print(research)

print("\nWRITER AGENT")
article = writer_agent(research)
print(article)

print("\nREVIEWER AGENT")
review = reviewer_agent(article)
print(review)
