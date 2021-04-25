}
Return only valid JSON."""

SAMPLE_TRANSCRIPT = """
Sarah: Alright everyone, let's get started. It's Monday the 3rd and we have John, Mike, and Lisa here.

John: Thanks Sarah. So the main thing I wanted to cover is the Q4 product roadmap.
We need to decide on the feature freeze date.

Sarah: I think we should freeze by November 15th. That gives QA three weeks before the holiday release.

Mike: That works for me. But we still need to finalize the payment integration. Lisa, where are you on that?

Lisa: I'm about 60% done. I need the API docs from the payment provider. I've emailed them twice but haven't heard back.

John: I'll escalate that today. I'll reach out to our account manager at PaymentCo. That's blocking us.

Sarah: Okay, so John will handle the PaymentCo escalation by end of today. Lisa continues on payment integration, targeting completion by November 10th.

Mike: I can help with testing once Lisa has a draft ready. Let's say I start testing November 11th.

Sarah: Great. Also, we decided to cut the social login feature from this release. Too risky to add now.

John: Agreed. We'll put it in Q1 backlog.

Sarah: Any other blockers? No? Okay. Same time next week, November 10th.
"""


def parse_json_response(text: str) -> dict:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
        cleaned = re.sub(r"\s*```$", "", cleaned)
    match = re.search(r"\{.*\}", cleaned, re.DOTALL)
    if match:
        cleaned = match.group(0)
    return json.loads(cleaned)
