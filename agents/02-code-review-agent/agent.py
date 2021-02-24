    group.add_argument("--code", help="Inline code snippet to review")
    parser.add_argument("--language", default="python", help="Programming language (default: python)")
    args = parser.parse_args()

    if args.file:
        with open(args.file) as f:
            code = f.read()
        print(f"\n🔍 Reviewing: {args.file}\n")
    else:
        code = args.code
        print(f"\n🔍 Reviewing inline code snippet\n")

    review = review_code(code, args.language)

    print("=" * 60)
    print("📋 CODE REVIEW")
    print("=" * 60)
    print(review)


if __name__ == "__main__":
    main()
