"""
PII Sanitization Agent — client for the TrustBoost API.

Removes sensitive data (emails, phones, national IDs, bank accounts,
API keys) from text before it reaches an LLM or external API. Built for
autonomous agent pipelines where human review is not possible.

This is a thin client: the sanitization logic, models, and on-chain
proof live behind the TrustBoost API. The agent demonstrates the
privacy/security pattern — call it on any user text before an LLM call.

Usage:
    python agent.py --text "Call me at 555-123-4567, email a@b.com"
    python agent.py --file input.txt
    python agent.py   # runs the built-in demo

Uses the free trial (50 sanitizations) when no API key / tx_hash is set.
"""

import argparse
import os
import sys
import json

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

import requests

API_BASE = os.environ.get("TRUSTBOOST_API_BASE", "https://api.trustboost.dev")
ENDPOINT = f"{API_BASE}/sanitize"


def sanitize(text: str, context: str = "general", tx_hash: str = "TRIAL") -> dict:
    """Send text to TrustBoost and return the sanitized result.
