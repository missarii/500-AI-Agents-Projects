
    response = llm.invoke(messages)
    return response.content


def main():
    parser = argparse.ArgumentParser(description="News Summarizer Agent")
    parser.add_argument("--topic", default="artificial intelligence", help="News topic to search")
    parser.add_argument("--count", type=int, default=5, help="Number of articles to fetch")
    args = parser.parse_args()

    print(f"\n📰 Fetching news about: {args.topic}\n")
    articles = fetch_news(args.topic, args.count)
    print(f"✅ Found {len(articles)} articles")

    summary = summarize_news(args.topic, articles)

    print("\n" + "=" * 60)
    print(f"📋 NEWS BRIEFING: {args.topic.upper()}")
    print("=" * 60)
    print(summary)


if __name__ == "__main__":
    main()
