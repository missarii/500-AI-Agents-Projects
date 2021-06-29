"""
Job Application Agent using CrewAI.

Analyzes a job description and a candidate profile, then generates:
- Tailored cover letter
- Resume bullet points to highlight
- Interview preparation questions

Usage:
    python agent.py --job-desc "Senior Python Engineer at Stripe..." --candidate "7 years Python, FastAPI..."
"""

import argparse
import os

from crewai import Agent, Crew, Process, Task
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

SAMPLE_JOB = """Senior Python Engineer at Stripe
We're looking for a Senior Python Engineer to join our API Platform team.

Requirements:
- 5+ years Python development
- Experience with distributed systems
- Strong understanding of REST APIs and microservices
- Experience with PostgreSQL, Redis
- Kubernetes experience preferred
