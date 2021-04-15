# Data Analysis Agent

Chat with your data. Load any CSV or Excel file and ask analytical questions in natural language.

**Framework**: LangChain (Pandas Agent)  
**LLM**: GPT-4o  

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
```

## Run

```bash
# Demo mode — creates sample sales data automatically
python agent.py --allow-dangerous-code
