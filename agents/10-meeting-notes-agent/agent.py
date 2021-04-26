def main():
    parser = argparse.ArgumentParser(description="Meeting Notes Agent")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--transcript", help="Path to transcript text file")
    group.add_argument("--text", help="Transcript text directly")
    parser.add_argument("--output", default="meeting_notes.md", help="Markdown output path")
    args = parser.parse_args()

    if args.transcript:
        with open(args.transcript) as f:
            transcript = f.read()
        print(f"\n📝 Processing: {args.transcript}\n")
    elif args.text:
        transcript = args.text
        print("\n📝 Processing transcript...\n")
    else:
        print("\n📝 Using sample meeting transcript\n")
        transcript = SAMPLE_TRANSCRIPT

    notes = generate_meeting_notes(transcript)
    formatted = format_notes(notes)

    print("=" * 60)
    print(formatted)
    print("=" * 60)

    # Save to file
    output_file = args.output
    if os.path.exists(output_file) and args.output == "meeting_notes.md":
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"meeting_notes_{stamp}.md"
    with open(output_file, "w") as f:
        f.write(formatted)
    print(f"\n✅ Saved to: {output_file}")


if __name__ == "__main__":
    main()
