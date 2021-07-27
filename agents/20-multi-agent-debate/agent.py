        print(f"\n--- Round {round_num} ---\n")

        pro_arg = pro.make_argument(topic, round_num, last_con_arg)
        print(f"🟢 {pro.name} (FOR):")
        print(pro_arg)

        con_arg = con.make_argument(topic, round_num, pro_arg)
        print(f"\n🔴 {con.name} (AGAINST):")
        print(con_arg)

        last_pro_arg = pro_arg
        last_con_arg = con_arg

    print(f"\n{'='*60}")
    print("🏛️  JUDGE'S VERDICT")
    print("=" * 60)
    verdict = judge.evaluate(topic, pro, con)
    print(verdict["verdict"])


def main():
    parser = argparse.ArgumentParser(description="Multi-Agent Debate System")
    parser.add_argument("--topic", default="AI will create more jobs than it eliminates over the next decade", help="Debate topic")
    parser.add_argument("--rounds", type=int, default=2, help="Number of debate rounds (1-4)")
    args = parser.parse_args()

    rounds = max(1, min(4, args.rounds))
    run_debate(args.topic, rounds)


if __name__ == "__main__":
    main()
