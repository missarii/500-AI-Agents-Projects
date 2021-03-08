    parser.add_argument("--db", default="demo.sqlite", help="SQLite database path")
    parser.add_argument("--question", help="Natural language question (omit for interactive)")
    parser.add_argument("--allow-write", action="store_true", help="Open the SQLite database read-write instead of read-only")
    args = parser.parse_args()

    if args.db == "demo.sqlite" and not os.path.exists("demo.sqlite"):
        print("🏗️  Creating demo e-commerce database...")
        create_demo_database("demo.sqlite")

    agent, db = build_agent(args.db, read_only=not args.allow_write)
    print(f"\n📊 Connected to: {args.db}")
    print(f"🔒 Mode: {'read-write' if args.allow_write else 'read-only'}")
    print(f"📋 Tables: {', '.join(db.get_table_names())}\n")

    if args.question:
        print(f"❓ Question: {args.question}")
        result = agent.invoke({"input": args.question})
        print(f"\n✅ Answer: {result['output']}")
    else:
        print("💬 SQL Agent ready. Ask questions in natural language. Type 'quit' to exit.\n")
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
