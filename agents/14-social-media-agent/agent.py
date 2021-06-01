"""
Social Media Content Agent using CrewAI.

Generates platform-optimized content (Twitter/X, LinkedIn, Instagram)
from a topic or article URL.

Usage:
    python agent.py --topic "The rise of AI agents in 2025"
    python agent.py --topic "New product launch: CloudSync Pro v3" --brand "CloudSync"
"""

import argparse
import os

from crewai import Agent, Crew, Process, Task
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def generate_social_content(topic: str, brand: str, platforms: list[str]) -> str:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

    strategist = Agent(
        role="Social Media Strategist",
        goal="Analyze the topic and define the key message, target audience, and tone for each platform",
        backstory="Award-winning social media strategist who has grown 50+ brand accounts to 100k+ followers.",
        llm=llm,
        verbose=False,
    )

