"""
Stock Research Agent using Agno + Yahoo Finance.

Provides comprehensive stock analysis: price data, financials,
analyst ratings, and AI-powered investment summary.

Usage:
    python agent.py --ticker AAPL
    python agent.py --ticker NVDA
"""

import argparse
import os

from dotenv import load_dotenv

load_dotenv()

try:
    import yfinance as yf
    HAS_YFINANCE = True
except ImportError:
    HAS_YFINANCE = False

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI


def get_stock_data(ticker: str) -> dict:
    if not HAS_YFINANCE:
        return {"ticker": ticker, "error": "yfinance not installed", "mock": True}

    stock = yf.Ticker(ticker)
    info = stock.info

    return {
