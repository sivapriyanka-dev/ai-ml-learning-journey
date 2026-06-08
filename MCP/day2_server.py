from mcp.server.fastmcp import FastMCP
print("FastMCP imported successfully")

mcp = FastMCP("Calculator Server")


@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b


@mcp.tool()
def subtract(a: int, b: int) -> int:
    return a - b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    return a * b


@mcp.tool()
def divide(a: int, b: int) -> float:
    return a / b


if __name__ == "__main__":
    print("Starting MCP Server...")
    mcp.run()
