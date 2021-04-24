"""
Meeting Notes Agent.

Converts meeting transcript text into structured meeting notes:
summary, action items, decisions, and follow-ups.

Usage:
    python agent.py --transcript meeting.txt
    python agent.py --text "John: Let's ship v2 next Friday..."
"""

import argparse
import json
import os
import re
from datetime import date, datetime

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

NOTES_PROMPT = """You are a professional meeting note-taker. Convert the meeting transcript into structured notes as JSON:
{
  "meeting_title": "inferred title",
  "date": "today or mentioned date",
  "participants": ["name1", "name2"],
  "duration_estimate": "X minutes",
  "summary": "2-3 sentence executive summary",
  "key_decisions": ["decision 1", "decision 2"],
  "action_items": [
    {"task": "description", "owner": "person name or TBD", "due": "date or timeframe or TBD"}
  ],
  "discussion_topics": ["topic 1", "topic 2"],
  "blockers": ["blocker 1 or none"],
  "next_meeting": "scheduled time or TBD",
  "follow_up_questions": ["question needing resolution"]
