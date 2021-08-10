    Keep it under 300 words, technical audience.""",
    expected_output="A concise technical briefing on AI agents in 2025",
    agent=researcher,
)

# 3. Create and run the crew
crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    process=Process.sequential,
    verbose=True,
)

if __name__ == "__main__":
    result = crew.kickoff()
    print("\n" + "=" * 60)
    print("FINAL RESULT:")
    print("=" * 60)
    print(result)
