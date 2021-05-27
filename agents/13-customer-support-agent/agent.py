"""
Customer Support Agent using LangGraph with RAG.

Handles customer queries using a knowledge base (product docs).
Routes complex issues to human escalation.

Usage:
    python agent.py
    python agent.py --kb-dir docs/          # load custom knowledge base
"""

import argparse
import os
from pathlib import Path
from typing import Annotated, Literal, TypedDict

from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages

load_dotenv()

SAMPLE_KB = [
    "Product: CloudSync Pro. Features: real-time sync across 5 devices, 1TB storage, offline mode, version history 30 days.",
    "Pricing: Basic $9/mo (100GB, 2 devices), Pro $19/mo (1TB, 5 devices), Business $49/mo (5TB, unlimited devices).",
    "Cancellation: Cancel anytime from Account > Subscription > Cancel. Refunds available within 14 days of charge.",
    "Password reset: Go to login page, click 'Forgot Password', enter email. Reset link expires in 1 hour.",
    "Sync issues: Check internet connection, ensure app is updated, try Sign Out and Sign In. If persists, contact support.",
    "Supported platforms: Windows 10+, macOS 12+, iOS 15+, Android 10+, Linux (Beta).",
    "Data security: AES-256 encryption at rest and in transit. SOC 2 Type II certified. Zero-knowledge architecture.",
    "File size limit: Individual files up to 10GB (Pro/Business), 2GB (Basic). No limit on total number of files.",
]

ESCALATION_KEYWORDS = ["refund", "lawsuit", "furious", "fraud", "broken", "data loss", "cancel account", "charge", "billing error"]

