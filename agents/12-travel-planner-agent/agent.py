"""
Travel Planner Agent using CrewAI.

Multi-agent crew that creates personalized travel itineraries:
- Destination Researcher: gathers destination info
- Activity Planner: creates day-by-day activities
- Budget Analyst: estimates costs

Usage:
    python agent.py --destination "Tokyo, Japan" --days 5 --budget 2000
"""

import argparse
import os

from crewai import Agent, Crew, Process, Task
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def build_travel_crew(destination: str, days: int, budget: float, interests: str) -> str:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.4)

    researcher = Agent(
        role="Destination Researcher",
        goal=f"Research {destination} and provide key travel insights",
        backstory="Expert travel journalist who has visited 100+ countries. Knows the best hidden gems and practical tips.",
        llm=llm,
        verbose=False,
    )

    planner = Agent(
        role="Travel Itinerary Planner",
