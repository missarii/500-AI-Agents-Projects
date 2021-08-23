
    @mcp.tool()
    def prioritize_tasks(tasks: list[str]) -> str:
        """
        Prioritize a list of tasks by estimated importance.

        Args:
            tasks: List of task descriptions to prioritize

        Returns:
            JSON string with prioritized tasks
        """
        prioritized = []
        for i, task in enumerate(tasks):
            priority = "HIGH" if i < len(tasks) // 3 else "MEDIUM" if i < 2 * len(tasks) // 3 else "LOW"
            prioritized.append({"rank": i + 1, "task": task, "priority": priority})
        return json.dumps(prioritized, indent=2)

    @mcp.tool()
    def format_as_json(data: dict) -> str:
        """
        Format data as pretty-printed JSON.

        Args:
            data: Dictionary to format

        Returns:
            Pretty-printed JSON string
        """
        return json.dumps(data, indent=2, default=str)

