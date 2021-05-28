{state['retrieved_context']}

Be friendly, concise, and solution-focused. If unsure, say so honestly."""),
            *conversation,
            HumanMessage(content=state["user_input"]),
        ]
        response = llm.invoke(messages)
        response_text = response.content

    return {"response": response_text, "messages": [AIMessage(content=response_text)]}


def route_after_escalation_check(state: SupportState) -> Literal["generate", "generate"]:
    return "generate"


def build_graph():
    graph = StateGraph(SupportState)
    graph.add_node("retrieve", retrieve_context)
    graph.add_node("check_escalation", check_escalation)
    graph.add_node("generate", generate_response)
    graph.set_entry_point("retrieve")
    graph.add_edge("retrieve", "check_escalation")
    graph.add_edge("check_escalation", "generate")
    graph.add_edge("generate", END)
    return graph.compile()


def load_kb_texts(kb_dir: str | None) -> list[str]:
    if not kb_dir:
        return SAMPLE_KB

    root = Path(kb_dir)
    if not root.is_dir():
        raise ValueError(f"Knowledge base directory does not exist: {kb_dir}")

    texts = []
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.suffix.lower() in {".txt", ".md"}:
            texts.append(path.read_text(encoding="utf-8"))
