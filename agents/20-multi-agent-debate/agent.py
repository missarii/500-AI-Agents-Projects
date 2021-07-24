CON arguments ({con_agent.name}):
{con_args}

Provide your verdict:"""),
        ])
        return {"verdict": response.content}


def run_debate(topic: str, rounds: int = 2) -> None:
    pro = DebateAgent(
        name="Dr. Alex Chen",
        position="FOR",
        expertise="technology economist and AI researcher"
    )
    con = DebateAgent(
        name="Prof. Sarah Martinez",
        position="AGAINST",
        expertise="labor economist and social policy expert"
    )
    judge = DebateJudge()

    print(f"\n{'='*60}")
    print(f"⚖️  DEBATE: {topic}")
    print(f"{'='*60}")
    print(f"🟢 FOR: {pro.name} ({pro.expertise})")
    print(f"🔴 AGAINST: {con.name} ({con.expertise})")
    print(f"🏛️  Rounds: {rounds}")
    print("=" * 60)

    last_con_arg = ""
    last_pro_arg = ""

    for round_num in range(1, rounds + 1):
