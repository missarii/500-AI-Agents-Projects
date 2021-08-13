
    editing_task = Task(
        description="""Review the article for:
        1. Accuracy (check facts align with research)
        2. Clarity (remove jargon, improve flow)
        3. Conciseness (trim wordiness)
        4. Add a compelling title and subtitle

        Return the final polished version.""",
        expected_output="Final edited article with title, subtitle, and polished content",
        agent=editor,
        context=[research_task, writing_task],
    )

    crew = Crew(
        agents=[researcher, writer, editor],
        tasks=[research_task, writing_task, editing_task],
        process=Process.sequential,
        verbose=True,
    )

    return str(crew.kickoff())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Multi-Agent Research & Writing Crew")
    parser.add_argument("--topic", default="AI agents in healthcare", help="Research topic")
    args = parser.parse_args()

    print(f"\n🚀 Starting crew for topic: {args.topic}\n")
    result = run_crew(args.topic)

    print("\n" + "=" * 60)
    print("FINAL ARTICLE:")
    print("=" * 60)
    print(result)
