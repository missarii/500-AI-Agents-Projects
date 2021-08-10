"""
Lesson 01: Your First CrewAI Agent

Demonstrates the fundamentals of CrewAI:
- Creating agents with roles, goals, and backstories
- Defining tasks
- Running a simple crew

Run: python agent.py
"""

from crewai import Agent, Crew, Process, Task
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

# 1. Define the agent
researcher = Agent(
    role="AI Researcher",
