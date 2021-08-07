```bash
python lesson_01/agent.py
python lesson_02/agent.py --topic "AI agents in healthcare"

# Lesson 03 includes a matching FastMCP server and CrewAI wrappers.
python lesson_03/agent.py
# Optional: inspect/run the FastMCP server separately:
python lesson_03/mcp_server.py
```

### Using uv (recommended modern method)

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver. To use uv:

1. Install uv:
```bash
pip install uv
```

2. Create and activate a virtual environment:
```bash
uv venv
source .venv/Scripts/activate
```

3. Install dependencies:
```bash
uv pip install -r lesson_01/requirements.txt
uv pip install -r lesson_02/requirements.txt
uv pip install -r lesson_03/requirements.txt
```

4. Set up your environment variables:
```bash
export OPENAI_API_KEY=your-openai-api-key
export MCP_SERVER_URL=http://localhost:8000
