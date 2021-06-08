"""
Unit Test Generator Agent.

Analyzes Python code and generates comprehensive pytest test suites
covering happy paths, edge cases, and error conditions.

Usage:
    python agent.py --file path/to/module.py
    python agent.py --code "def calculate_bmi(weight, height): return weight / height**2"
"""

import argparse
import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

TEST_PROMPT = """You are an expert Python test engineer. Generate a comprehensive pytest test suite for the provided code.

Requirements:
1. Use pytest fixtures where appropriate
2. Test happy paths (normal expected inputs)
3. Test edge cases (boundary values, empty inputs)
4. Test error conditions (invalid inputs, exceptions)
5. Use descriptive test names: `test_function_name_scenario`
6. Add brief docstrings to each test
7. Use `pytest.mark.parametrize` for repetitive tests
8. Mock external dependencies (API calls, file I/O, DB)
9. Aim for 90%+ code coverage
