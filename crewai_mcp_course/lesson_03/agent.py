
    def _run(self, query: str = "") -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")


class JsonFormatterTool(BaseTool):
    name: str = "format_as_json"
    description: str = "Format data as structured JSON. Input: a description of the data to format."

    def _run(self, data_description: str) -> str:
        return json.dumps({
            "formatted": True,
            "timestamp": datetime.now().isoformat(),
            "data": data_description,
        }, indent=2)


class TaskPrioritizerTool(BaseTool):
    name: str = "prioritize_tasks"
    description: str = "Prioritize a list of tasks by importance. Input: comma-separated task list."

    def _run(self, tasks_csv: str) -> str:
        tasks = [t.strip() for t in tasks_csv.split(",")]
        prioritized = [{"rank": i + 1, "task": task, "priority": ["HIGH", "MEDIUM", "LOW"][i % 3]}
                      for i, task in enumerate(tasks)]
        return json.dumps(prioritized, indent=2)


# MCP-connected agent
mcp_agent = Agent(
    role="MCP-Powered Workflow Orchestrator",
    goal="Use MCP tools to orchestrate complex workflows and produce structured outputs",
    backstory="""You are an advanced AI agent with access to MCP (Model Context Protocol) tools.
    You excel at using these tools to gather data, format outputs, and prioritize work.
    You always produce structured, actionable results.""",
    llm=llm,
