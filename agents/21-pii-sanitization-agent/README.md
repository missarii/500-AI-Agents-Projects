```

With no API key it uses the **free trial** (50 sanitizations, `tx_hash=TRIAL`).
For higher volume, pay once via x402 and pass the Solana tx hash:

```bash
export TRUSTBOOST_WALLET="<your-agent-wallet>"
python agent.py --text "..." --tx-hash "<solana_tx_hash>"
```

Sanitize a file:

```bash
python agent.py --file input.txt --context legal
```

Context modes: `general | financial | legal | medical | code`.

## Sample output

```json
{
  "status": "success",
  "data": {
    "sanitized_content": "Hi, I'm [REDACTED]. My email is [REDACTED] and my phone is [REDACTED]. RFC: [REDACTED]. Account [REDACTED]. API key [REDACTED].",
    "safety_score": 0.6,
    "risk_category": "PRIVATE",
