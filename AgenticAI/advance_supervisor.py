import ollama


# ======================
# RESEARCH AGENT
# ======================

def research_agent(task):

    prompt = f"""
    Give important research points about:

    {task}
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

def writer_agent(task):

    prompt = f"""
    Write a short article about:

    {task}
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

def reviewer_agent(task):

    prompt = f"""
    Review the following content
    and suggest improvements:

    {task}
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
# SUPERVISOR
# ======================

def supervisor(task):

    task_lower = task.lower()

    if "research" in task_lower:

        print("\nSupervisor → Research Agent")

        return research_agent(task)

    elif "write" in task_lower:

        print("\nSupervisor → Writer Agent")

        return writer_agent(task)

    elif "review" in task_lower:

        print("\nSupervisor → Reviewer Agent")

        return reviewer_agent(task)

    return "No suitable agent found."


# ======================
# TESTS
# ======================

tasks = [
    "Research Agentic AI",
    "Write article about Machine Learning",
    "Review this article about AI"
]

for task in tasks:

    print("\n" + "=" * 60)

    print("\nTask:")
    print(task)

    result = supervisor(task)

    print("\nResult:")
    print(result)
