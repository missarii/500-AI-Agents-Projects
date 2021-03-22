        # Return mock data if no API key
        return [
            {"title": f"Major development in {topic}", "description": f"Researchers announce breakthrough in {topic} field.", "url": "https://example.com/1", "source": {"name": "Tech News"}},
            {"title": f"{topic.title()} industry sees rapid growth", "description": f"New report shows {topic} adoption up 40% year-over-year.", "url": "https://example.com/2", "source": {"name": "Business Daily"}},
            {"title": f"Experts weigh in on {topic} challenges", "description": f"Leading experts discuss obstacles facing the {topic} space.", "url": "https://example.com/3", "source": {"name": "Science Weekly"}},
        ]

    url = f"https://newsapi.org/v2/everything?q={topic}&language=en&pageSize={count}&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    response = requests.get(url, timeout=10)
    data = response.json()
    return data.get("articles", [])


def summarize_news(topic: str, articles: list[dict]) -> str:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    articles_text = "\n\n".join(
        f"Title: {a['title']}\nSource: {a.get('source', {}).get('name', 'Unknown')}\nSummary: {a.get('description', 'N/A')}"
        for a in articles[:5]
    )

    messages = [
        SystemMessage(content="You are a news analyst. Create a structured news briefing with: 1) Top Story, 2) Key Themes (3 bullet points), 3) What to Watch, 4) Quick Headlines list."),
        HumanMessage(content=f"Topic: {topic}\n\nArticles:\n{articles_text}"),
    ]
