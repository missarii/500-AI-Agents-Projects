        verbose=False,
    )

    writer = Agent(
        role="Career Coach and Application Writer",
        goal="Create tailored application materials that maximize interview chances",
        backstory="Career coach who has helped 500+ candidates land roles at top tech companies.",
        llm=llm,
        verbose=False,
    )

    analyst_task = Task(
        description=f"""Analyze this job description:
{job_desc}

Extract: top 5 required skills, culture signals, what this company values most, potential red flags, and key phrases to mirror in the application.""",
        agent=analyst,
        expected_output="Job analysis: key requirements, culture signals, important keywords",
    )

    application_task = Task(
        description=f"""Using the job analysis, create application materials for this candidate:
{candidate_profile}

Produce:
1. COVER LETTER (250-300 words, 3 paragraphs: hook, evidence, close)
2. TOP 5 RESUME BULLETS TO HIGHLIGHT (tailored to this specific role)
3. 10 LIKELY INTERVIEW QUESTIONS (5 behavioral, 5 technical) with suggested answer frameworks
4. NEGOTIATION RANGE ESTIMATE based on role seniority and company""",
        agent=writer,
        expected_output="Cover letter, resume bullets, interview questions, salary range",
