from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Resource Server")


# ==========================
# RESOURCE 1
# ==========================

@mcp.resource("notes://all")
def get_notes():

    with open(
        "notes.txt",
        "r"
    ) as file:

        return file.read()


# ==========================
# RESOURCE 2
# ==========================

@mcp.resource("user://profile")
def get_user():

    with open(
        "user_data.txt",
        "r"
    ) as file:

        return file.read()


# ==========================
# TOOL
# ==========================

@mcp.tool()
def add(a: int, b: int):

    return a + b


# ==========================
# SERVER
# ==========================

if __name__ == "__main__":

    print(
        "Starting Resource MCP Server..."
    )

    mcp.run()
