        "ticker": ticker,
        "name": info.get("longName", ticker),
        "sector": info.get("sector", "N/A"),
        "industry": info.get("industry", "N/A"),
        "price": info.get("currentPrice", info.get("regularMarketPrice", 0)),
        "market_cap": info.get("marketCap", 0),
        "pe_ratio": info.get("trailingPE", "N/A"),
        "forward_pe": info.get("forwardPE", "N/A"),
        "peg_ratio": info.get("pegRatio", "N/A"),
        "revenue_growth": info.get("revenueGrowth", "N/A"),
        "profit_margin": info.get("profitMargins", "N/A"),
        "dividend_yield": info.get("dividendYield", 0),
        "52w_high": info.get("fiftyTwoWeekHigh", "N/A"),
        "52w_low": info.get("fiftyTwoWeekLow", "N/A"),
        "analyst_rating": info.get("recommendationKey", "N/A"),
        "target_price": info.get("targetMeanPrice", "N/A"),
        "description": info.get("longBusinessSummary", "")[:500],
    }


def analyze_stock(data: dict) -> str:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    stock_info = "\n".join(f"{k}: {v}" for k, v in data.items() if k != "description")

    messages = [
        SystemMessage(content="You are a financial analyst. Provide a concise stock analysis covering: Investment Thesis (2-3 sentences), Key Strengths (3 bullets), Key Risks (3 bullets), Valuation Assessment, and a Verdict (Buy/Hold/Sell with brief reasoning). Keep it under 300 words."),
        HumanMessage(content=f"Analyze this stock:\n{stock_info}\n\nCompany description: {data.get('description', 'N/A')}"),
    ]

    response = llm.invoke(messages)
    return response.content


def format_number(n) -> str:
    if isinstance(n, (int, float)):
        if n >= 1e12:
