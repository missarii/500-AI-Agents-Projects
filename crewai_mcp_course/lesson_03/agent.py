        - Executive Summary: 2-3 sentences

        Make it professional and actionable.""",
        expected_output="Professional project status report",
        agent=coordinator,
        context=[gather_task],
    )

    crew = Crew(
        agents=[mcp_agent, coordinator],
        tasks=[gather_task, report_task],
        process=Process.sequential,
        verbose=True,
    )

    return str(crew.kickoff())


if __name__ == "__main__":
    project = "AI Agent Platform v2.0"
    tasks = [
        "Implement RAG pipeline",
        "Write unit tests",
        "Deploy to staging",
        "Update documentation",
        "Security audit",
        "Performance benchmarking",
    ]

    print(f"\n🔗 Running MCP-powered CrewAI workflow for: {project}\n")
    result = run_mcp_workflow(project, tasks)

    print("\n" + "=" * 60)
    print("PROJECT STATUS REPORT:")
    print("=" * 60)
    print(result)
