# Build an AI Agent

This repository contains the exercises, projects, and notes developed throughout the **Build an AI Agent** course from [Boot.dev](https://www.boot.dev/).

The goal of this course is to learn, through hands-on development, how to build an **AI agent** from the ground up, exploring concepts such as LLMs, tool calling, context management, command execution, and agent loops.

## 🚀 About the Project

This project follows the development of an **AI Agent** capable of receiving instructions in natural language, reasoning about them, and taking actions through a set of available tools.

Instead of simply interacting with a language model, the goal is to build a system capable of **reasoning about a task, using tools, processing their results, and producing a final response**.

## 📚 Topics Covered

Throughout the course, the following concepts are explored:

* Large Language Models (LLMs)
* AI APIs
* Prompt engineering
* Context and messages
* Tool calling
* Function-based tools
* Agent execution loops
* File manipulation
* Command execution
* Error handling
* Context management
* AI agent architecture
* Integrating LLMs with application code

## 🛠️ Technologies

* **Python**
* **LLM / AI APIs**
* **Git & GitHub**
* **Boot.dev**

## 📁 Project Structure

```text
.
├── main.py
├── functions/
│   └── ...
├── prompts/
│   └── ...
├── tests/
│   └── ...
├── requirements.txt
└── README.md
```

> The project structure may change as the course progresses and new features are introduced.

## ⚙️ Installation

Clone the repository:

```bash
git clone <REPOSITORY_URL>
cd <REPOSITORY_NAME>
```

Create a virtual environment:

```bash
python -m venv venv
```

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

If the project requires an AI API, configure the required environment variables.

Create a `.env` file:

```env
API_KEY=your_api_key_here
```

**Never commit API keys or other secrets to the repository.**

Add the following to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
```

## ▶️ Running the Project

With the virtual environment activated, run:

```bash
python main.py
```

The agent will then be able to receive instructions and use the implemented tools to perform the requested tasks.

## 🧠 How It Works

At a high level, the agent follows a loop similar to this:

```text
User
  │
  ▼
┌──────────────┐
│     LLM      │
└──────┬───────┘
       │
       ▼
  Does it need
     a tool?
     │
  ┌──┴───┐
  │      │
 No     Yes
  │      │
  ▼      ▼
Response  Tool
           │
           ▼
         Result
           │
           └──────► LLM
                     │
                     ▼
               Final Response
```

The agent operates in a loop where the model analyzes the user's request, determines whether a tool is needed, receives the tool's result, and continues processing until it can provide a final response.

## 🎯 Learning Goals

By completing this course, the main goals are to:

* Understand how LLM-powered applications work
* Build an AI agent from scratch
* Learn how LLMs interact with external tools
* Implement an agent loop
* Work with APIs and structured data
* Improve Python programming skills
* Understand the fundamentals of agentic AI systems

## 📌 Course

This project is part of the **Build an AI Agent** course by Boot.dev.

More information about the course can be found on [Boot.dev](https://www.boot.dev/).

## 📄 License

This repository is intended for educational purposes and contains my own implementations and notes developed while following the course.
