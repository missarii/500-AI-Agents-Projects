    response = llm.invoke(messages)
    return parse_json_response(response.content)


def score_fit(profile: dict, job_desc: str) -> dict:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    messages = [
        SystemMessage(content=FIT_PROMPT),
        HumanMessage(content=f"Candidate profile:\n{json.dumps(profile, indent=2)}\n\nJob description:\n{job_desc}"),
    ]
    response = llm.invoke(messages)
    return parse_json_response(response.content)


SAMPLE_RESUME = """
Jane Doe
jane.doe@email.com | +1 (555) 123-4567 | San Francisco, CA
linkedin.com/in/janedoe | github.com/janedoe

SUMMARY
Senior Python developer with 7 years of experience building scalable web applications
and data pipelines. Led teams of 5-8 engineers at Series B startups.

EXPERIENCE
Senior Software Engineer | TechCorp Inc. | 2021-present
- Architected microservices platform handling 10M requests/day using FastAPI + Kubernetes
- Reduced API latency by 40% through Redis caching and async optimization
- Led migration from monolith to microservices (12-month project, 5 engineers)

Software Engineer | DataFlow Systems | 2018-2021
- Built ML data pipelines processing 500GB/day using Apache Spark and Airflow
- Developed REST APIs with Django REST Framework serving 50k daily users

SKILLS
Languages: Python, JavaScript, SQL, Bash
Frameworks: FastAPI, Django, React, Spark
Tools: Docker, Kubernetes, Redis, PostgreSQL, Git, Airflow
Cloud: AWS (EC2, S3, RDS, Lambda)

EDUCATION
B.S. Computer Science | UC Berkeley | 2017

CERTIFICATIONS
