```bash
# Default example
python agent.py

# Custom email
python agent.py \
  --context "Apologize for the delayed delivery of the software project" \
  --tone "apologetic but confident" \
  --recipient "the client project manager"
```

## Architecture

```
Context → [Analyst Agent] → Email Brief → [Writer Agent] → Final Email
```
