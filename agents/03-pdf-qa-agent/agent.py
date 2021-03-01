"""
PDF Q&A Agent using LlamaIndex.

Loads a PDF, indexes it, and answers questions about its content.
Maintains conversation history for follow-up questions.

Usage:
    python agent.py --pdf path/to/document.pdf
    python agent.py --pdf report.pdf --question "What is the main finding?"
"""

import argparse
import os

from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.llms.openai import OpenAI

load_dotenv()


def build_index(pdf_path: str) -> VectorStoreIndex:
    print(f"📄 Loading and indexing {pdf_path}...")
    reader = SimpleDirectoryReader(input_files=[pdf_path])
    docs = reader.load_data()
