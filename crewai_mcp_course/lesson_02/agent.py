"""
Lesson 02: Multi-Agent Crew with Tool Use

Demonstrates:
- Multiple specialized agents with different roles
- Custom tools (web search, calculator)
- Sequential and hierarchical processes
- Agent collaboration patterns

Run: python agent.py --topic "quantum computing applications"
"""

import argparse
import os

from crewai import Agent, Crew, Process, Task
from crewai.tools import BaseTool
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import Field

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)


# Custom Tool: Word Counter
class WordCountTool(BaseTool):
    name: str = "word_counter"
    description: str = "Count words in a text string. Input: text string."

    def _run(self, text: str) -> str:
        count = len(text.split())
        return f"Word count: {count}"


