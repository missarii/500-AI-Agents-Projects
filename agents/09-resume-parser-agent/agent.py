}
Return only valid JSON."""

FIT_PROMPT = """Given this candidate profile and job description, return JSON:
{
  "fit_score": 0-100,
  "fit_label": "Excellent|Good|Fair|Poor",
  "strengths": ["matching point 1", "matching point 2", ...],
  "gaps": ["missing skill 1", ...],
  "recommendation": "Hire|Consider|Pass",
  "recommendation_reason": "2-3 sentence explanation"
}
Return only valid JSON."""


def parse_json_response(text: str) -> dict:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
        cleaned = re.sub(r"\s*```$", "", cleaned)
    match = re.search(r"\{.*\}", cleaned, re.DOTALL)
    if match:
        cleaned = match.group(0)
    return json.loads(cleaned)


def read_resume_text(path: str) -> str:
    if path.endswith(".pdf"):
        try:
            import pypdf
            with open(path, "rb") as f:
                reader = pypdf.PdfReader(f)
                return "\n".join(page.extract_text() for page in reader.pages)
        except ImportError:
            print("⚠️  pypdf not installed. Install with: pip install pypdf")
            raise
    with open(path) as f:
        return f.read()


def parse_resume(text: str) -> dict:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    messages = [SystemMessage(content=PARSE_PROMPT), HumanMessage(content=text)]
