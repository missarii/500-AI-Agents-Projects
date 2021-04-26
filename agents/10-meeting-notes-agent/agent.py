

def generate_meeting_notes(transcript: str) -> dict:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    messages = [
        SystemMessage(content=NOTES_PROMPT),
        HumanMessage(content=f"Meeting transcript:\n\n{transcript}"),
    ]
    response = llm.invoke(messages)
    return parse_json_response(response.content)


def format_notes(notes: dict) -> str:
    lines = [
        f"# {notes.get('meeting_title', 'Meeting Notes')}",
        f"**Date:** {notes.get('date', date.today().isoformat())}  |  **Duration:** {notes.get('duration_estimate', 'N/A')}",
        f"**Participants:** {', '.join(notes.get('participants', []))}",
        "",
        "## Summary",
        notes.get("summary", ""),
        "",
        "## Key Decisions",
        *[f"- {d}" for d in notes.get("key_decisions", [])],
        "",
        "## Action Items",
    ]
    for item in notes.get("action_items", []):
        lines.append(f"- [ ] **{item.get('task', 'Task')}** — Owner: {item.get('owner', 'TBD')} | Due: {item.get('due', 'TBD')}")

    if notes.get("blockers"):
        lines += ["", "## Blockers", *[f"- {b}" for b in notes["blockers"]]]

    if notes.get("next_meeting") and notes["next_meeting"] != "TBD":
        lines += ["", f"**Next Meeting:** {notes['next_meeting']}"]

    return "\n".join(lines)


