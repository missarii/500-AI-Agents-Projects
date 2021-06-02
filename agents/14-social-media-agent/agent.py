
    crew = Crew(
        agents=[strategist, writer],
        tasks=[strategy_task, writing_task],
        process=Process.sequential,
        verbose=False,
    )

    return str(crew.kickoff())


def main():
    parser = argparse.ArgumentParser(description="Social Media Content Agent")
    parser.add_argument("--topic", default="How AI is transforming software development in 2025", help="Content topic")
    parser.add_argument("--brand", default="", help="Brand name (optional)")
    parser.add_argument("--platforms", default="twitter,linkedin,instagram", help="Comma-separated platforms")
    args = parser.parse_args()

    platforms = [p.strip() for p in args.platforms.split(",")]
    print(f"\n📱 Generating content for: {', '.join(platforms)}")
    print(f"📌 Topic: {args.topic}\n")

    content = generate_social_content(args.topic, args.brand, platforms)

    print("=" * 60)
    print("✍️  SOCIAL MEDIA CONTENT")
    print("=" * 60)
    print(content)


if __name__ == "__main__":
    main()
