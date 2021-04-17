AWS Solutions Architect Associate
"""


def main():
    parser = argparse.ArgumentParser(description="Resume Parser Agent")
    parser.add_argument("--resume", help="Path to resume file (.txt or .pdf)")
    parser.add_argument("--job-desc", help="Job description to match against")
    args = parser.parse_args()

    if args.resume:
        print(f"\n📄 Parsing resume: {args.resume}")
        text = read_resume_text(args.resume)
    else:
        print("\n📄 Using sample resume (pass --resume to use your own)")
        text = SAMPLE_RESUME

    profile = parse_resume(text)

    print("\n" + "=" * 60)
    print("👤 PARSED RESUME")
    print("=" * 60)
    print(f"Name: {profile.get('name')}")
    print(f"Title: {profile.get('current_title')}")
    print(f"Experience: {profile.get('years_experience')} years")
    print(f"Skills: {', '.join(profile.get('skills', {}).get('languages', []))}")
    print(f"\nSummary: {profile.get('summary')}")

    if args.job_desc:
        print("\n" + "=" * 60)
        print("📊 JOB FIT ANALYSIS")
        print("=" * 60)
        fit = score_fit(profile, args.job_desc)
        fit_label = fit.get("fit_label", "N/A")
        label_emoji = {"Excellent": "🟢", "Good": "🟡", "Fair": "🟠", "Poor": "🔴"}.get(fit_label, "⚪")
        print(f"{label_emoji} Fit Score: {fit.get('fit_score', 'N/A')}/100 ({fit_label})")
        print(f"✅ Strengths: {', '.join(fit.get('strengths', [])[:3])}")
        print(f"⚠️  Gaps: {', '.join(fit.get('gaps', ['None identified'])[:3])}")
        print(f"🎯 Recommendation: {fit.get('recommendation', 'N/A')}")
        print(f"💭 {fit.get('recommendation_reason', 'N/A')}")


if __name__ == "__main__":
    main()
