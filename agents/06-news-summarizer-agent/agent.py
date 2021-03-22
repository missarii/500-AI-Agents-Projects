"""
News Summarizer Agent using AutoGen.

Fetches news articles and produces structured summaries with key insights.

Usage:
    python agent.py --topic "artificial intelligence"
    python agent.py --topic "climate change" --count 5
"""

import argparse
import os

import requests
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def fetch_news(topic: str, count: int = 5) -> list[dict]:
    if not NEWS_API_KEY:
