from datetime import datetime
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Personal MCP Server")


# ==========================
# CALCULATOR
# ==========================

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two numbers
    """
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers
    """
    return a * b


# ==========================
# WEATHER
# ==========================

@mcp.tool()
def weather(city: str) -> str:
    """
    Get weather information
    """

    data = {
        "hyderabad": "34°C Sunny",
        "bangalore": "28°C Cloudy",
        "mumbai": "31°C Rainy"
    }

    return data.get(
        city.lower(),
        "Weather data unavailable"
    )


# ==========================
# CURRENT TIME
# ==========================

@mcp.tool()
def current_time() -> str:
    """
    Get current time
    """

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


# ==========================
# NOTES
# ==========================

notes_storage = []


@mcp.tool()
def save_note(note: str) -> str:
    """
    Save note
    """

    notes_storage.append(note)

    return "Note saved."


@mcp.tool()
def get_notes() -> list:
    """
    Get all notes
    """

    return notes_storage


# ==========================
# START SERVER
# ==========================

if __name__ == "__main__":

    print("Starting Personal MCP Server...")

    mcp.run()
