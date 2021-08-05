# PII Sanitization Agent

Removes sensitive data from text **before** it reaches an LLM or external API.
Built for autonomous agent pipelines where human review is not possible.

The agent calls the [TrustBoost](https://api.trustboost.dev) API, which detects
and redacts PII (emails, phones, national IDs, bank accounts, API keys) and
returns a structured, auditable result. This is a thin client: the detection
models, multilingual support, and on-chain proof of sanitization live behind the
API, so no PII-handling code or weights live in this repo.

## Why it matters

PII leaking through autonomous pipelines is a real gap — an agent that forwards
user text to an LLM can accidentally expose emails, phones, tax IDs, or secrets.
This agent is the guardrail: sanitize first, then send.

- Semantic PII detection (well above regex-only accuracy)
- Multilingual: EN, ES-LATAM, PT-BR, DE, JA
- LATAM identifiers: RFC, CPF, CUIT, RUT
- Fail-closed: on any API/transport error it returns `[REDACTED]`, never raw PII
- Audit trail: no raw PII is stored by the agent; optional on-chain proof available

## Quick start

```bash
pip install -r requirements.txt
python agent.py --text "Call me at 555-123-4567, email a@b.com, RFC PEMJ880126MNEZSN01"
