class MCPServer:

    def calculator(self, a, b):
        return a + b


class MCPClient:

    def __init__(self, server):
        self.server = server

    def ask(self):
        return self.server.calculator(
            10,
            20
        )


server = MCPServer()

client = MCPClient(server)

print(
    client.ask()
)
