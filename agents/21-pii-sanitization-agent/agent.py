        "risk_category": "CRITICAL",
        "sanitized_content": "[REDACTED — unexpected response]",
        "http_status": resp.status_code,
    }


DEMO_TEXT = (
    "Hi, I'm Juan Pérez. My email is juan.perez@example.com and my phone is "
    "+1-555-123-4567. RFC: PEMJ880126MNEZSN01. Account 0123456789. "
    "API key sk-abc123fakekeynotreal0000000000."
)


def main():
    ap = argparse.ArgumentParser(description="PII Sanitization Agent (TrustBoost client)")
    ap.add_argument("--text", help="text to sanitize")
    ap.add_argument("--file", help="path to a text file to sanitize")
    ap.add_argument("--context", default="general", help="general|financial|legal|medical|code")
    ap.add_argument("--tx-hash", default="TRIAL", help="TRIAL for free tier, or Solana tx hash")
    args = ap.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()
    elif args.text:
        text = args.text
    else:
        text = DEMO_TEXT
        print("No --text/--file provided. Running built-in demo.\n")

    print("INPUT :", text[:120] + ("..." if len(text) > 120 else ""))
    result = sanitize(text, context=args.context, tx_hash=args.tx_hash)
    print("\nRESULT :")
    print(json.dumps(result, indent=2, ensure_ascii=False)[:800])


if __name__ == "__main__":
    main()
