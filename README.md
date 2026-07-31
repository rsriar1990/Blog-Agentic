# Blog-Agentic

An AI-powered blog generation system built using LangGraph and Large Language Models (LLMs). The application orchestrates multiple AI agents to research, generate, refine, and translate blog content through a graph-based workflow.

---

## Features

- Agentic workflow powered by LangGraph
- Modular node-based architecture
- Multi-stage blog generation
- Translation support
- Extensible LLM integration
- Stateful workflow execution
- REST API support
- Postman collection for API testing

---

## Project Structure

```
Blog-Agentic/
│
├── src/
│   ├── graphs/          # LangGraph workflow definitions
│   ├── llms/            # LLM providers and configuration
│   ├── nodes/           # Agent nodes for each workflow step
│   ├── states/          # Shared workflow state models
│
├── postman/             # API collections
├── .langgraph_api/      # LangGraph configuration
├── README.md
└── requirements.txt
```

---

## Architecture

The application follows an Agentic AI architecture.

```
User Request
      │
      ▼
 Graph Controller
      │
      ▼
 Title Generation Agent
      │
      ▼
 Blog content Generation Agent
      │
      ▼
 Translation Agent
      │
      ▼
 Review / Final Output
```

Each step is implemented as a LangGraph node that shares information through a centralized workflow state.

---

## Technologies

- Python
- LangGraph
- LangChain
- Groq / LLM APIs
- FastAPI
- Uvicorn
- Postman

---

## Installation

Clone the repository.

```bash
git clone https://github.com/rsriar1990/Blog-Agentic.git

cd Blog-Agentic
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file.

Example:

```env
GROQ_API_KEY=your_api_key
LANGCHAIN_API_KEY=your_langchain_key
```

---

## Running the Application

```bash
python app.py
```


## Workflow

1. User submits a topic.
2. Research agent gathers context and create title.
3. Content generation agent creates the draft.
4. Translation agent converts the blog into the requested language.
5. Final response is returned.

---

## API

Example request

```http
POST /blogs
```

Request

```json
{
    "topic": "Artificial Intelligence",
    "language": "french"
}
```

Example response

```json
{
    "title": "...",
    "content": "...",
    "translated": true
}
```

---

## Extending the Project

New agents can be added by:

- Creating a new node under `src/nodes`
- Updating the graph inside `src/graphs`
- Extending the workflow state if required

---

## Author

Randeep

GitHub:
https://github.com/rsriar1990