    tools=[DateTimeTool(), JsonFormatterTool(), TaskPrioritizerTool()],
    verbose=True,
)

# Coordinator agent
coordinator = Agent(
    role="Project Coordinator",
    goal="Coordinate tasks and produce a final project status report",
    backstory="Experienced project manager who synthesizes information into clear status reports.",
    llm=llm,
    verbose=True,
)


def run_mcp_workflow(project_name: str, tasks: list[str]) -> str:
    tasks_str = ", ".join(tasks)

    gather_task = Task(
        description=f"""For project "{project_name}", use your MCP tools to:
        1. Get the current datetime using get_datetime tool
        2. Prioritize these tasks using prioritize_tasks tool: {tasks_str}
        3. Format the results as JSON using format_as_json tool

        Return all gathered information.""",
        expected_output="Current time, prioritized task list, and formatted data",
        agent=mcp_agent,
    )

    report_task = Task(
        description=f"""Create a project status report for "{project_name}" using the gathered data.

        Report format:
        - Project: {project_name}
        - Generated: [timestamp from data]
        - Status: Active
        - Task Priority Matrix: [use the prioritized tasks]
        - Next Action: [highest priority incomplete task]
