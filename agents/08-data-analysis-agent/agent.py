    if not args.allow_dangerous_code:
        print("⚠️  This agent uses LangChain's pandas agent, which executes model-generated Python code.")
        print("Run again with --allow-dangerous-code only with trusted prompts and non-sensitive data.")
        return

    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=False,
        allow_dangerous_code=args.allow_dangerous_code,
    )

    if args.question:
        print(f"❓ Question: {args.question}")
        result = agent.invoke({"input": args.question})
        print(f"\n✅ Answer: {result['output']}")
    else:
        print("💬 Data Analysis Agent ready. Ask questions about your data. Type 'quit' to exit.\n")
        print("Example questions:")
        print("  - What is the total revenue by product?")
        print("  - Which region has the highest average order value?")
        print("  - Show me the top 5 sales days\n")
        while True:
            question = input("You: ").strip()
            if question.lower() in ("quit", "exit", "q"):
                break
            if not question:
                continue
            result = agent.invoke({"input": question})
            print(f"\nAgent: {result['output']}\n")


if __name__ == "__main__":
    main()
