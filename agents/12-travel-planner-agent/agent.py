        goal=f"Create a detailed {days}-day itinerary for {destination}",
        backstory="Luxury travel consultant with 15 years of experience crafting personalized itineraries.",
        llm=llm,
        verbose=False,
    )

    budget_analyst = Agent(
        role="Travel Budget Analyst",
        goal=f"Estimate realistic costs for the trip within ${budget} budget",
        backstory="Financial travel advisor who helps travelers maximize experiences within budget.",
        llm=llm,
        verbose=False,
    )

    research_task = Task(
        description=f"""Research {destination} for a {days}-day trip.
Cover: best time to visit, neighborhoods to stay in, must-see attractions,
local food scene, transportation tips, and cultural customs to know.
Traveler interests: {interests}""",
        agent=researcher,
        expected_output="Destination brief with key areas, attractions, food, and practical tips",
    )

    planning_task = Task(
        description=f"""Create a {days}-day itinerary for {destination}.
Budget: ${budget} total. Interests: {interests}.
Include morning/afternoon/evening activities, specific restaurant recommendations,
and travel time between locations. Make it achievable and enjoyable.""",
        agent=planner,
        expected_output=f"Day-by-day {days}-day itinerary with activities, meals, and timing",
        context=[research_task],
    )

    budget_task = Task(
        description=f"""Provide a budget breakdown for the {days}-day {destination} trip.
Total budget: ${budget}. Include: flights (estimate), accommodation, food, activities,
