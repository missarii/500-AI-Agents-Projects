- Strong communication skills

Responsibilities:
- Design and build high-performance APIs handling millions of requests/day
- Lead technical design reviews
- Mentor junior engineers
- Collaborate with product managers on technical feasibility
"""

SAMPLE_CANDIDATE = """
Jane Doe — 7 years Python experience
Current role: Senior Software Engineer at DataCorp
Skills: Python, FastAPI, Django, PostgreSQL, Redis, Docker, Kubernetes, AWS
Achievements:
- Built API platform handling 5M requests/day
- Led team of 4 engineers
- Reduced API latency by 40%
- Mentored 3 junior engineers
Education: BS Computer Science, UC Berkeley
"""


def run_job_application_crew(job_desc: str, candidate_profile: str) -> str:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.4)

    analyst = Agent(
        role="Job Requirements Analyst",
        goal="Analyze the job description and identify key requirements, values, and culture signals",
        backstory="Ex-hiring manager at FAANG with 10 years recruiting experience. Expert at decoding job descriptions.",
        llm=llm,
