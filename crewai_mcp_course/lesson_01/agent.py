    goal="Research and summarize the latest developments in AI agents",
    backstory="""You are a seasoned AI researcher who stays up-to-date with
    the latest papers, frameworks, and applications in the AI agent space.
    You write clear, accurate summaries for technical audiences.""",
    llm=llm,
    verbose=True,
)

# 2. Define the task
research_task = Task(
    description="""Research and write a concise briefing on:
    "The current state of AI agents in 2025"

    Cover:
    - What are AI agents and why they matter
    - Top 3 frameworks (CrewAI, LangGraph, AutoGen)
    - 2 real-world use cases making impact
    - What's coming next

