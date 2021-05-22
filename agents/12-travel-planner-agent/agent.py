transportation. Flag if budget is tight and suggest adjustments.""",
        agent=budget_analyst,
        expected_output="Itemized budget breakdown with daily averages and money-saving tips",
        context=[research_task, planning_task],
    )

    crew = Crew(
        agents=[researcher, planner, budget_analyst],
        tasks=[research_task, planning_task, budget_task],
        process=Process.sequential,
        verbose=False,
    )

    return str(crew.kickoff())


def main():
    parser = argparse.ArgumentParser(description="Travel Planner Agent")
    parser.add_argument("--destination", default="Tokyo, Japan", help="Travel destination")
    parser.add_argument("--days", type=int, default=7, help="Number of days")
    parser.add_argument("--budget", type=float, default=3000, help="Total budget in USD")
    parser.add_argument("--interests", default="food, culture, history", help="Traveler interests")
    args = parser.parse_args()

    print(f"\n✈️  Planning {args.days}-day trip to {args.destination} (Budget: ${args.budget})\n")
    itinerary = build_travel_crew(args.destination, args.days, args.budget, args.interests)

    print("=" * 60)
    print("🗺️  TRAVEL ITINERARY")
    print("=" * 60)
    print(itinerary)


if __name__ == "__main__":
    main()
