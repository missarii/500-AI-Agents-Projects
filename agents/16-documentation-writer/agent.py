"""
Documentation Writer Agent.

Generates comprehensive documentation for Python modules:
README, API reference, docstrings, and usage examples.

Usage:
    python agent.py --file path/to/module.py
    python agent.py --file src/utils.py --format readme
"""

import argparse
import ast
import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()


def extract_structure(code: str) -> str:
    """Extract functions, classes, and their signatures from Python code."""
    try:
        tree = ast.parse(code)
        structure = []

        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                args = [a.arg for a in node.args.args]
                prefix = "async def" if isinstance(node, ast.AsyncFunctionDef) else "def"
                structure.append(f"{prefix} {node.name}({', '.join(args)})")
            elif isinstance(node, ast.ClassDef):
                structure.append(f"class {node.name}:")
                for item in node.body:
                    if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        args = [a.arg for a in item.args.args]
                        prefix = "async def" if isinstance(item, ast.AsyncFunctionDef) else "def"
                        structure.append(f"  {prefix} {item.name}({', '.join(args)})")

        return "\n".join(structure)
    except Exception:
        return "Could not parse structure"


README_PROMPT = """You are a technical documentation expert. Generate a complete, professional README.md for this Python module.

Include:
