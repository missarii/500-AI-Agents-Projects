"""
SQL Query Agent using LangChain.

Connects to a SQLite database and answers natural language questions
by generating and executing SQL queries.

Usage:
    python agent.py                          # uses demo database
    python agent.py --db path/to/db.sqlite   # your database
    python agent.py --db mydb.sqlite --question "How many users signed up last month?"
"""

import argparse
import os
import sqlite3
from urllib.parse import quote

from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType

load_dotenv()


def create_demo_database(db_path: str):
    """Creates a demo e-commerce SQLite database for testing."""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.executescript("""
