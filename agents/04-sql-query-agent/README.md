# SQL Query Agent

Connects to any SQLite database and answers natural language questions by generating and executing SQL.

**Framework**: LangChain  
**LLM**: GPT-4o-mini  

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
```

## Run

```bash
# Demo mode — creates a sample e-commerce database automatically
python agent.py

# Your own database
