    query_engine = index.as_query_engine(similarity_top_k=5)
    response = query_engine.query(question)
    print("\n" + "=" * 60)
    print("📋 ANSWER")
    print("=" * 60)
    print(response.response)
    if hasattr(response, "source_nodes"):
        print(f"\n📚 Sources: {len(response.source_nodes)} chunk(s) referenced")


def main():
    parser = argparse.ArgumentParser(description="PDF Q&A Agent")
    parser.add_argument("--pdf", required=True, help="Path to PDF file")
    parser.add_argument("--question", help="Single question (omit for interactive mode)")
    args = parser.parse_args()

    index = build_index(args.pdf)

    if args.question:
        single_question(index, args.question)
    else:
        interactive_qa(index)


if __name__ == "__main__":
    main()
