# What is Agentic AI?

Agentic AI refers to artificial intelligence systems that possess agency, meaning they can act autonomously and make decisions based on their own goals and motivations. These systems are designed to operate independently, without constant human supervision
or intervention. Agentic AI can learn from its environment, adapt to new situations, and take actions to achieve specific objectives. This type of AI is often associated with advanced machine learning techniques and is used in various applications, including robotics, autonomous vehicles, and intelligent virtual assistants.
Agentic AI is characterized by its ability to perceive its surroundings, process information, and make informed decisions. It can interact with the environment, learn from experience, and improve its performance over time. This makes agentic AI a powerful tool for solving complex problems and performing tasks that require a high level of autonomy and adaptability.
Agentic AI can be categorized into different types based on its level of autonomy and capabilities. Some examples include:

1. Reactive Agents: These agents respond to stimuli in their environment without maintaining an internal state or memory. They make decisions based solely on the current input.
2. Deliberative Agents: These agents have an internal model of the world and can plan their actions based on that model. They can consider future consequences and make decisions accordingly.
3. Hybrid Agents: These agents combine reactive and deliberative capabilities, allowing them to respond quickly to immediate stimuli while also planning for long-term goals.
4. Learning Agents: These agents can learn from their experiences and improve their performance over time. They can adapt to changing environments and optimize their behavior based on feedback.
   Overall, agentic AI represents a significant advancement in artificial intelligence, enabling machines to operate with greater autonomy and intelligence. It has the potential to revolutionize various industries and improve the way we interact with technology.

Traditional LLM
Example:
User: What is the weather in New York?
LLM: I don't know current weather.
Why? Because LLM only knows what was in training data.

Agent = LLM + Tools + Decision Making
Example:
User:What is the weather in New York?
Agent thinks:
Need weather data
Use weather tool
Get response
Return answer

User
↓
LLM
↓
Decide Tool
↓
Weather API
↓
Result
↓
Final Answer
This ability to reason and act is why it's called Agentic AI.

# Core Components of an Agent

1. Brain: The LLM
   Examples:
   GPT
   Claude
   Gemini
   Llama

2. Memory: Stores context.
   Example: User: My name is Priyanka
   Later...
   User: What is my name?
   Agent:
   Your name is Priyanka.

3. Tools: External capabilities.
   Examples:
   Calculator
   Search
   Database
   APIs
   Email

4. Planning: Breaks tasks into steps.
   Example: Book trip to Hyderabad
   Plan:
   Step 1: Find flights
   Step 2: Find hotels
   Step 3: Create itinerary

ReAct Pattern: Most agents use:
Re = Reason - Think about next action.
Act = Act - Call tool.
Example:
Question:What is 56 × 89?
Thought:Need calculator.
Action:calculator(56\*89)
Observation:4984
Answer:4984
This cycle repeats until task is completed.

# Agent Dynamic path

Input
↓
Think
↓
Choose Tool
↓
Think Again
↓
Choose Another Tool
↓
Output

- **Perception**: The agent must be able to perceive its environment through sensors or data inputs. This could include visual, auditory, or textual information.
- **Reasoning**: The agent must be able to process the information it receives and make decisions based on that information. This involves logical reasoning, problem-solving, and decision-making capabilities.
- **Action**: The agent must be able to take actions based on its decisions. This could involve physical actions (in the case of robots) or digital actions (such as sending a message or making an API call).
- **Learning**: The agent should be able to learn from its experiences and improve its performance over time. This could involve machine learning techniques or reinforcement learning.
- **Goal-Oriented Behavior**: The agent should have specific goals or objectives that it strives to achieve. This allows it to make decisions and take actions that are aligned with its goals.

# Applications of Agentic AI

Agentic AI has a wide range of applications across various industries. Some examples include:

1. **Autonomous Vehicles**: Agentic AI can be used to develop self-driving cars that can navigate and make decisions on the road without human intervention.
2. **Robotics**: Agentic AI can be used to create robots that can perform tasks autonomously, such as cleaning, delivery, or manufacturing.
3. **Virtual Assistants**: Agentic AI can be used to develop intelligent virtual assistants that can understand and respond to user queries, manage schedules, and perform tasks on behalf of the user.
4. **Healthcare**: Agentic AI can be used to develop systems that can assist with diagnosis, treatment planning, and patient monitoring.
5. **Finance**: Agentic AI can be used to develop systems that can analyze financial data, make investment decisions, and manage portfolios.
6. **Customer Service**: Agentic AI can be used to develop chatbots and virtual agents that can handle customer inquiries and provide support.
   Overall, agentic AI has the potential to revolutionize various industries and improve the way we interact with technology. It enables machines to operate with greater autonomy and intelligence, allowing them to perform complex tasks and solve problems in ways that were previously not possible.

# Day 2: Tool Calling & Function Calling.

A tool is simply a function the AI can use.
Example:
Tool: calculator(a,b)
Description: Takes two numbers and returns their product.
Agent: What is 56 × 89?
Agent thinks:
Need calculator.
Agent calls calculator(56,89)
Agent gets response: 4984
Agent returns answer: 4984
In this example, the agent recognizes that it needs to use the calculator tool to answer the question. It calls the calculator function with the appropriate arguments (56 and 89) and receives the response (4984). Finally, it returns the answer to the user. This process demonstrates how agentic AI can utilize tools to enhance its capabilities and provide accurate responses to user queries.

Real-World Examples

- Search Tool : search("Latest AI news")
- Weather Tool : weather("New York")
- Database Tool : get_customer(123)
- Email Tool : send_email(...)

Agents become powerful because they can use many tools.

1. **ChatGPT with Plugins**: ChatGPT can use plugins to access external tools and services. For example, it can use a plugin to access a weather API to provide current weather information to users.
2. **ReAct Agents**: ReAct agents use a combination of reasoning and acting to solve complex problems. They can call various tools and functions to gather information, perform calculations, and make decisions based on the data they receive.
3. **Autonomous Robots**: Autonomous robots can use various tools and functions to navigate their environment, manipulate objects, and perform tasks. For example, a robot in a warehouse might use a tool to scan barcodes and a function to calculate the optimal path for picking items.
4. **Virtual Assistants**: Virtual assistants like Siri or Alexa can call various functions to perform tasks for users. For example, they can call a function to set reminders, play music, or control smart home devices.
   Overall, the ability to call tools and functions is a crucial aspect of agentic AI, allowing it to extend its capabilities and provide more comprehensive and accurate responses to user queries.

flow:
User Question
↓
Agent
↓
Need Tool?
↙ ↘
Yes No
↓ ↓
Calculator Direct Answer
↓
Result

# Day 3 — Real LLM Tool Calling

User
↓
LLM
↓
Chooses Tool
↓
Tool Executes
↓
LLM Generates Answer

The AI itself decides when to use a tool.
This is how:
OpenAI Agents
LangGraph
CrewAI
MCP
actually work.

# Day 3 Deliverable

✅ Calculator Tool
✅ Year Tool
✅ Normal Chat

Example:

What is 25 \* 16?
→ Calculator

What year is it?
→ Year Tool

What is AI?
→ Normal LLM Response

# Day 4 — ReAct Agent (Reason → Act → Observe)

What is ReAct?
Most modern agents use this loop:

Question
↓
Reason
↓
Act (Use Tool)
↓
Observe Result
↓
Reason Again
↓
Final Answer

Example:
User: What is (25 \* 16) + 100? Agent goes

Thought:Need calculator.
Action:25 \* 16
Observation:400
Thought:Need another calculation.
Action:400 + 100
Observation:500
Final Answer:500

Notice:
The agent doesn't jump directly to the answer. It thinks between actions. This is the foundation of:
LangGraph
CrewAI
AutoGen
OpenAI Agents

# Week 2 — LangGraph Fundamentals

What is LangGraph?

Think of it as:

React → Frontend Apps
PyTorch → Deep Learning
LangGraph → AI Agents

Most companies building agents today use:

LangGraph
LangChain
OpenAI Agents SDK

And LangGraph is becoming the industry standard.

Day 1 — Nodes and Edges
Traditional Program
Start
↓
Function A
↓
Function B
↓
End
LangGraph
Node A
↓
Node B
↓
Node C

Each node performs a task.

Edges connect nodes.

# Message State & Memory

Understand why agents need memory.

Without memory:
User: My name is Priyanka
User: What is my name?
Agent:
I don't know.
With memory:
User: My name is Priyanka
User: What is my name?
Agent:
Your name is Priyanka.

# Tool Executor Node

So far you have:

User
↓
LLM Node
↓
Answer

Today:

User
↓
Router
↓
Tool Executor
↓
Answer

This is the core pattern used by:

LangGraph
OpenAI Agents
CrewAI
MCP Servers

Why Tool Executor?

Instead of:

if tool == "calculator":
...
if tool == "search":
...
if tool == "year":
...

Create a registry:

tools = {
"calculator": calculator,
"search": search,
"year": year
}

Now any tool can be executed dynamically.
