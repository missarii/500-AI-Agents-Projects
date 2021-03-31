    args = parser.parse_args()

    if args.issue_url:
        print(f"\n🔍 Fetching issue from GitHub...")
        title, body, labels = fetch_github_issue(args.issue_url)
    else:
        title, body, labels = args.title, args.body, []

    print(f"\n🏷️  Triaging: {title}\n")
    result = triage_issue(title, body, labels)

    severity = result.get("severity", "medium")
    labels = result.get("labels", [])
    severity_emoji = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢"}.get(severity, "⚪")

    print("=" * 60)
    print("📋 TRIAGE REPORT")
    print("=" * 60)
    print(f"{severity_emoji} Severity: {severity.upper()} (Priority: {result.get('priority_score', 'N/A')}/10)")
    print(f"📁 Category: {result.get('category', 'N/A')}")
    print(f"👤 Assignee: {result.get('assignee_type', 'any')} team")
    print(f"🏷️  Labels: {', '.join(labels)}")
    print(f"📝 Summary: {result.get('summary', 'N/A')}")
    print(f"❓ Needs more info: {'Yes' if result.get('needs_more_info') else 'No'}")
    print(f"🔍 Reproduction clear: {'Yes' if result.get('reproduction_clear') else 'No'}")
    print(f"\n💭 Notes: {result.get('triage_notes', 'N/A')}")


if __name__ == "__main__":
    main()
