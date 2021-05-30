
    if not texts:
        raise ValueError(f"No .txt or .md files found in knowledge base directory: {kb_dir}")

    return texts


def main():
    parser = argparse.ArgumentParser(description="Customer Support Agent")
    parser.add_argument("--kb-dir", help="Directory containing .txt or .md support knowledge base files")
    args = parser.parse_args()

    retrieve_context.kb_texts = load_kb_texts(args.kb_dir)
    if hasattr(retrieve_context, "vectorstore"):
        delattr(retrieve_context, "vectorstore")

    agent = build_graph()
    state = {"messages": [], "user_input": "", "retrieved_context": "", "response": "", "escalate": False}

    print("\n🎧 Customer Support Agent (CloudSync Pro)")
    print("Type 'quit' to exit\n")

    while True:
        user_input = input("Customer: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            break
        if not user_input:
            continue

        state["user_input"] = user_input
        state["messages"].append(HumanMessage(content=user_input))
        state = agent.invoke(state)

        escalation_indicator = " [ESCALATED]" if state.get("escalate") else ""
        print(f"\nAgent{escalation_indicator}: {state['response']}\n")


if __name__ == "__main__":
    main()
