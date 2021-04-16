"""
Resume Parser Agent using LangChain.

Extracts structured information from resume text or PDF:
contact info, skills, experience, education, and provides
a candidate summary and fit score for a job description.

Usage:
    python agent.py --resume resume.txt
    python agent.py --resume resume.pdf --job-desc "Senior Python Developer with 5+ years..."
"""

import argparse
import json
import os
import re

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

PARSE_PROMPT = """Extract structured information from this resume and return JSON:
{
  "name": "full name",
  "email": "email or null",
  "phone": "phone or null",
  "location": "city, country or null",
  "linkedin": "URL or null",
  "github": "URL or null",
  "summary": "2-3 sentence professional summary",
  "years_experience": number,
  "current_title": "current/most recent job title",
  "skills": {
    "languages": ["Python", "JavaScript", ...],
    "frameworks": ["Django", "React", ...],
    "tools": ["Docker", "Git", ...],
    "soft_skills": ["leadership", ...]
  },
  "experience": [{"title": "...", "company": "...", "duration": "...", "highlights": ["..."]}],
  "education": [{"degree": "...", "institution": "...", "year": "..."}],
  "certifications": ["..."],
  "languages_spoken": ["English", ...]
