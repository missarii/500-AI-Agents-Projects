
    Args:
        text: raw text that may contain PII
        context: general | financial | legal | medical | code
        tx_hash: "TRIAL" for the free tier, or a Solana tx hash after payment
    """
    payload = {
        "text": text,
        "tx_hash": tx_hash,
        "wallet_address": os.environ.get("TRUSTBOOST_WALLET", "demo-agent"),
        "context": context,
    }
    try:
        resp = requests.post(ENDPOINT, json=payload, timeout=30)
    except requests.RequestException as e:
        # Fail closed: do NOT return raw PII on transport error.
        return {
            "status": "error",
            "risk_category": "CRITICAL",
            "sanitized_content": "[REDACTED — sanitization service unreachable]",
            "error": str(e),
        }

    if resp.status_code == 200:
        return resp.json()

    if resp.status_code == 402:
        # Payment required — the service is live but needs a paid tx_hash.
        return {
            "status": "payment_required",
            "risk_category": "CRITICAL",
            "sanitized_content": "[REDACTED — payment required to sanitize]",
            "detail": resp.json().get("error", "Payment required"),
        }

    # Any other failure: fail closed.
    return {
        "status": "error",
