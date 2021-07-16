    competitor_analyses: dict[str, str]
    final_report: str


def identify_competitors(state: AnalysisState) -> AnalysisState:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    response = llm.invoke([
        SystemMessage(content="You are a market research analyst. List exactly 5 main competitors as a comma-separated list. Nothing else."),
        HumanMessage(content=f"Company: {state['company']}\nIndustry: {state['industry']}\n\nList 5 main competitors:"),
    ])
    competitors = [c.strip() for c in response.content.split(",")][:5]
    return {"competitors": competitors, "messages": [response]}


def analyze_competitor(state: AnalysisState) -> AnalysisState:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    analyses = {}

    for competitor in state["competitors"]:
        response = llm.invoke([
            SystemMessage(content="Provide a concise competitive analysis in 100 words covering: main products, strengths (2), weaknesses (2), pricing model, target market."),
            HumanMessage(content=f"Analyze {competitor} vs {state['company']} in {state['industry']}:"),
        ])
        analyses[competitor] = response.content

    return {"competitor_analyses": analyses}


def generate_report(state: AnalysisState) -> AnalysisState:
