    @mcp.tool()
    def calculate_project_metrics(tasks_completed: int, tasks_total: int) -> dict:
        """
        Calculate project completion metrics.

        Args:
            tasks_completed: Number of completed tasks
            tasks_total: Total number of tasks

        Returns:
            Dictionary with completion percentage and status
        """
        percentage = (tasks_completed / tasks_total * 100) if tasks_total > 0 else 0
        status = "On Track" if percentage >= 50 else "At Risk" if percentage >= 25 else "Behind"
        return {
            "completed": tasks_completed,
            "total": tasks_total,
            "percentage": round(percentage, 1),
            "status": status,
        }

    return mcp


if __name__ == "__main__":
    mcp = create_mcp_server()
    if mcp:
        print("🚀 MCP Server starting on localhost:8000")
        print("Tools available: get_datetime, prioritize_tasks, format_as_json, calculate_project_metrics")
        mcp.run(transport="streamable-http", host="localhost", port=8000)
    else:
        print("Install fastmcp to run the server: pip install fastmcp")
