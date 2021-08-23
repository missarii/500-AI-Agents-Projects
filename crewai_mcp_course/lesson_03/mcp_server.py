"""
FastMCP Server for Lesson 03.

Exposes tools that CrewAI agents can call via the MCP protocol.
This is the server side — agents connect to this to use the tools.

Run: python mcp_server.py
(Keep this running while agent.py is running)
"""

import json
from datetime import datetime

try:
    from fastmcp import FastMCP
    HAS_FASTMCP = True
except ImportError:
    HAS_FASTMCP = False
    print("FastMCP not installed. Run: pip install fastmcp")
    print("Showing example server code only.\n")


def create_mcp_server():
    if not HAS_FASTMCP:
        return None

    mcp = FastMCP("CrewAI Course Tools")

    @mcp.tool()
    def get_datetime() -> str:
        """Get the current date and time in UTC."""
        return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
