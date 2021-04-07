"""
Data Analysis Agent using LangChain + pandas.

Loads a CSV/Excel file and answers analytical questions about it using
natural language. The agent generates Python/pandas code to answer questions.

Usage:
    python agent.py --file data.csv
    python agent.py --file sales.xlsx --question "What is the monthly revenue trend?"
"""

import argparse
import os

import pandas as pd
from dotenv import load_dotenv
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI

load_dotenv()


def create_sample_data(path: str):
    """Creates a sample sales dataset for demo."""
    import random
    from datetime import date, timedelta

    random.seed(42)
    rows = []
    products = ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"]
    regions = ["North", "South", "East", "West"]
    start = date(2024, 1, 1)

    for i in range(200):
        d = start + timedelta(days=random.randint(0, 364))
