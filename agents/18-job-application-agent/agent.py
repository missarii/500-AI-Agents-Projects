        context=[analyst_task],
    )

    crew = Crew(
        agents=[analyst, writer],
        tasks=[analyst_task, application_task],
        process=Process.sequential,
        verbose=False,
    )

    return str(crew.kickoff())


def main():
    parser = argparse.ArgumentParser(description="Job Application Agent")
    parser.add_argument("--job-desc", default=SAMPLE_JOB, help="Job description text")
    parser.add_argument("--candidate", default=SAMPLE_CANDIDATE, help="Candidate profile summary")
    args = parser.parse_args()

    print("\n💼 Preparing job application materials...\n")
    result = run_job_application_crew(args.job_desc, args.candidate)

    print("=" * 60)
    print("📋 JOB APPLICATION PACKAGE")
    print("=" * 60)
    print(result)


if __name__ == "__main__":
    main()
