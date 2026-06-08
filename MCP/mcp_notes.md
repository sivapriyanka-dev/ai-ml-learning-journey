# MCP (Model Context Protocol)

MCP provides a standard protocol that allows AI applications to access tools, resources, and prompts without building custom integrations for each application.

This is probably the most important new AI protocol to learn in 2026.

Why MCP Exists

Before MCP:

OpenAI Agent
↓
Custom Code
↓
Weather API

Claude
↓
Different Custom Code
↓
Weather API

Every AI application needed its own integration.

With MCP:

OpenAI
↓
MCP
↓
Weather Tool

Claude
↓
MCP
↓
Weather Tool

Local Agent
↓
MCP
↓
Weather Tool

One protocol.

Many AI applications.

Think of MCP Like USB

Before USB:

Keyboard
Mouse
Printer

Different ports

After USB:

Everything
↓
USB

MCP is the USB for AI tools.

MCP Architecture
AI Client
↓
MCP Client
↓
MCP Server
↓
Tools
Resources
Prompts
Three Core Concepts

1. Tools

Things AI can execute.

Examples:

calculator()
weather()
search()
send_email() 2. Resources

Things AI can read.

Examples:

notes.txt
database
pdf
documents 3. Prompts

Reusable instructions.

Example:

Summarize this document
Real Example

User:

What's the weather in Hyderabad?

Flow:

Claude
↓
MCP Client
↓
Weather MCP Server
↓
Weather Tool
↓
Result

# MCP:

1. Receives the request from the AI client (Claude).
2. Translates the request into a standardized format.
3. Routes the request to the appropriate tool (Weather Tool).
4. Executes the tool and retrieves the result.
5. Sends the result back to the AI client (Claude).
