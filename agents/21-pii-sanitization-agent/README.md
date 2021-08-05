    "entities": [
      {"type": "email", "category": "PRIVATE"},
      {"type": "phone", "category": "PRIVATE"},
      {"type": "national_id", "category": "PRIVATE"}
    ]
  }
}
```

(Runtime: ~2–5 s per call depending on network. End-to-end demo under 10 min.)

## Ethical considerations

- Raw input is never stored by this agent. Sanitized output may be retained by the
  API provider for 90 days for audit; see the TrustBoost privacy docs.
- Fails closed on API error — it will not emit raw PII if the service is unreachable.
- Human oversight is recommended for high-risk deployments (healthcare, finance, legal).
- The included `sk-abc123fakekeynotreal0000000000` in sample text is a **fake** fixture,
  exactly what the redactor should catch.

## Compliance context

EU AI Act, GDPR, HIPAA, LGPD. Use this agent wherever agent-to-agent or
agent-to-LLM text carries user data.

## License

MIT (repository root). The TrustBoost API is a separate service; see its terms.
