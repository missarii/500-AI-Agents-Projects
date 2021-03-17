
    crew = Crew(
        agents=[analyst, writer],
        tasks=[analyze_task, write_task],
        process=Process.sequential,
        verbose=False,
    )

    result = crew.kickoff()
    return str(result)


def main():
    parser = argparse.ArgumentParser(description="Email Drafting Agent")
    parser.add_argument("--context", default="Follow up on our product demo from last Tuesday. They seemed interested but haven't responded.", help="Email context/purpose")
    parser.add_argument("--tone", default="professional and friendly", help="Email tone")
    parser.add_argument("--recipient", default="a potential client", help="Who the email is for")
    args = parser.parse_args()

    print(f"\n✉️  Drafting email...\n")
    email = build_email_crew(args.context, args.tone, args.recipient)

    print("=" * 60)
    print("📧 DRAFTED EMAIL")
    print("=" * 60)
    print(email)


if __name__ == "__main__":
    main()
