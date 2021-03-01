    index = VectorStoreIndex.from_documents(docs)
    print(f"✅ Indexed {len(docs)} document chunk(s)")
    return index


def interactive_qa(index: VectorStoreIndex):
    llm = OpenAI(model="gpt-4o-mini", temperature=0)
    memory = ChatMemoryBuffer.from_defaults(token_limit=4096)
    chat_engine = index.as_chat_engine(
        chat_mode="context",
        llm=llm,
        memory=memory,
        verbose=False,
    )

    print("\n💬 PDF Q&A Agent ready. Type 'quit' to exit.\n")
    while True:
        question = input("You: ").strip()
        if question.lower() in ("quit", "exit", "q"):
            break
        if not question:
            continue
        response = chat_engine.chat(question)
        print(f"\nAgent: {response.response}\n")


def single_question(index: VectorStoreIndex, question: str):
