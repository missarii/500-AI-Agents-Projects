        with open(args.file) as f:
            code = f.read()
        module_name = os.path.splitext(os.path.basename(args.file))[0]
        print(f"\n🧪 Generating tests for: {args.file}")
    elif args.code:
        code = args.code
        module_name = "module"
        print(f"\n🧪 Generating tests for inline code")
    else:
        code = SAMPLE_CODE
        module_name = "shopping"
        print(f"\n🧪 Generating tests for sample code")

    tests = generate_tests(code, module_name)

    # Clean up markdown fences if present
    if tests.startswith("```"):
        lines = tests.split("\n")
        tests = "\n".join(lines[1:-1] if lines[-1] == "```" else lines[1:])

    output_file = args.output or f"test_{module_name}.py"
    with open(output_file, "w") as f:
        f.write(tests)

    print(f"\n✅ Tests saved to: {output_file}")
    print(f"\nRun with: pytest {output_file} -v")
    print("\n" + "=" * 60)
    print(tests[:500] + "..." if len(tests) > 500 else tests)


if __name__ == "__main__":
    main()
