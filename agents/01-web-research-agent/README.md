# Web Research Agent

A LangGraph agent that searches the web for any topic and synthesizes a structured research report.

**Framework**: LangGraph  
**LLM**: GPT-4o-mini (OpenAI)  
**Search**: Tavily

## What it does

1. Takes a research query
2. Searches the web using Tavily (5 results)
3. Synthesizes findings into a structured report (Summary, Key Findings, Sources)

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your API keys
```
