    goal="Review and polish content for clarity, accuracy, and conciseness",
    backstory="Senior editor who ensures all content meets the highest quality standards.",
    llm=llm,
    verbose=True,
)


def run_crew(topic: str) -> str:
    research_task = Task(
        description=f"""Research the topic: "{topic}"

        Find:
        1. Core definition and key concepts (3 bullet points)
        2. Current applications (3 real examples)
        3. Future potential (2 predictions)
        4. Key challenges or limitations

        Use the word_counter tool to verify your output is under 250 words.""",
        expected_output="Research brief with definitions, applications, and future outlook",
        agent=researcher,
    )

    writing_task = Task(
        description=f"""Transform the research into an engaging technical article about "{topic}".

        Structure:
        - Hook opening (1-2 sentences)
        - What it is (clear definition)
        - Why it matters (use formatter tool for 3 key benefits as numbered list)
        - Real-world impact (2 examples)
        - Call to action closing

        Target: 200-250 words, technical but accessible.""",
        expected_output="Polished technical article ready for publication",
        agent=writer,
        context=[research_task],
    )
