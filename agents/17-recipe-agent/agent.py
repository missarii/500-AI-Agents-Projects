"""
Recipe Recommendation Agent using Agno-style single agent.

Suggests recipes based on available ingredients, dietary restrictions,
and time constraints.

Usage:
    python agent.py --ingredients "chicken, garlic, lemon, rosemary"
    python agent.py --ingredients "tofu, broccoli, soy sauce" --diet vegan --time 20
"""

import argparse
import json
import os
import re

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

RECIPE_PROMPT = """You are a professional chef and nutritionist. Given available ingredients and constraints,
suggest 3 recipes. Return JSON:
{
  "recipes": [
    {
      "name": "Recipe Name",
      "cuisine": "Italian/Asian/etc",
      "difficulty": "Easy/Medium/Hard",
      "prep_time": "X minutes",
