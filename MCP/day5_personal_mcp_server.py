from datetime import datetime
from mcp.server.fastmcp import FastMCP
import json

mcp = FastMCP("Personal MCP Server")

# ==================================
# IN-MEMORY STORAGE
# ==================================

notes_storage = []
todo_storage = []

# ==================================
# TOOLS
# ==================================


@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    return a * b


@mcp.tool()
def weather(city: str) -> str:

    data = {
        "hyderabad": "34°C Sunny",
        "bangalore": "28°C Cloudy",
        "mumbai": "31°C Rainy"
    }

    return data.get(
        city.lower(),
        "Weather unavailable"
    )


@mcp.tool()
def current_time() -> str:

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


@mcp.tool()
def save_note(note: str) -> str:

    notes_storage.append(note)

    return "Note saved."


@mcp.tool()
def get_notes() -> list:

    return notes_storage


@mcp.tool()
def add_todo(task: str) -> str:

    todo_storage.append(task)

    return "Todo added."


@mcp.tool()
def get_todos() -> list:

    return todo_storage


# ==================================
# RESOURCES
# ==================================

@mcp.resource("notes://all")
def notes_resource():

    with open(
        "notes.txt",
        "r"
    ) as file:

        return file.read()


@mcp.resource("tasks://all")
def tasks_resource():

    with open(
        "tasks.txt",
        "r"
    ) as file:

        return file.read()


@mcp.resource("user://profile")
def user_resource():

    with open(
        "user_data.txt",
        "r"
    ) as file:

        return file.read()


@mcp.resource("config://app")
def config_resource():

    with open(
        "config.json",
        "r"
    ) as file:

        return json.load(file)


# ==================================
# SERVER
# ==================================

if __name__ == "__main__":

    print(
        "Starting Personal MCP Server..."
    )

    mcp.run()
