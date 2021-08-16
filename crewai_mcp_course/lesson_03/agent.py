"""
Lesson 03: CrewAI + FastMCP Integration

Demonstrates:
- Building a FastMCP server that exposes tools
- Mirroring MCP server tools as CrewAI BaseTool wrappers
- Production pattern: keep tool contracts stable between MCP server and CrewAI wrappers

Architecture:
    MCP Server tool contracts → CrewAI tool wrappers → Output

Run the agent: python agent.py
Optional: run python mcp_server.py to inspect the matching FastMCP server tools.
"""

import asyncio
import json
import os
from datetime import datetime

from crewai import Agent, Crew, Process, Task
from crewai.tools import BaseTool
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import Field

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)


# CrewAI tool wrappers that mirror the FastMCP server's tool contracts.
# In production, replace these wrappers with a real MCP client adapter.
class DateTimeTool(BaseTool):
    name: str = "get_datetime"
    description: str = "Get the current date and time"
