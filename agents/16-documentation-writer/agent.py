        if not re.search(r'[A-Z]', password):
            return False, "Password must contain at least one uppercase letter"
        if not re.search(r'\d', password):
            return False, "Password must contain at least one digit"
        return True, ""
'''


def main():
    parser = argparse.ArgumentParser(description="Documentation Writer Agent")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--file", help="Python file to document")
    group.add_argument("--code", help="Inline code to document")
    parser.add_argument("--format", choices=["readme", "docstrings", "both"], default="both", help="Documentation format to generate")
    args = parser.parse_args()

    if args.file:
        with open(args.file) as f:
            code = f.read()
        filename = os.path.basename(args.file)
    elif args.code:
        code = args.code
        filename = "module.py"
    else:
        code = SAMPLE_CODE
        filename = "validators.py"
        print("\n📝 Using sample validators module")

    print(f"\n✍️  Generating documentation for: {filename}\n")

    if args.format in ("readme", "both"):
        print("📄 Generating README...")
        readme = generate_readme(code, filename)
        readme_file = f"README_{filename.replace('.py', '')}.md"
        with open(readme_file, "w") as f:
            f.write(readme)
        print(f"✅ README saved to: {readme_file}")

    if args.format in ("docstrings", "both"):
        print("📝 Adding docstrings...")
        documented_code = add_docstrings(code, filename)
        output_file = f"documented_{filename}"
        with open(output_file, "w") as f:
            f.write(documented_code)
        print(f"✅ Documented code saved to: {output_file}")


if __name__ == "__main__":
    main()
