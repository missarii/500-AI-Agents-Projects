            return f"${n/1e12:.2f}T"
        if n >= 1e9:
            return f"${n/1e9:.2f}B"
        if n >= 1e6:
            return f"${n/1e6:.2f}M"
        return f"${n:.2f}"
    return str(n)


def main():
    parser = argparse.ArgumentParser(description="Stock Research Agent")
    parser.add_argument("--ticker", required=True, help="Stock ticker symbol (e.g., AAPL)")
    args = parser.parse_args()

    print(f"\n📈 Researching {args.ticker}...\n")

    data = get_stock_data(args.ticker)

    print("=" * 60)
    print(f"📊 {data.get('name', args.ticker)} ({args.ticker})")
    print("=" * 60)
    print(f"Price: ${data.get('price', 'N/A')}  |  Market Cap: {format_number(data.get('market_cap', 0))}")
    print(f"Sector: {data.get('sector')}  |  Industry: {data.get('industry')}")
    print(f"P/E: {data.get('pe_ratio')}  |  Forward P/E: {data.get('forward_pe')}  |  PEG: {data.get('peg_ratio')}")
    print(f"52W Range: ${data.get('52w_low')} - ${data.get('52w_high')}")
    analyst_rating = data.get("analyst_rating") or "N/A"
    print(f"Analyst: {str(analyst_rating).upper()}  |  Target: ${data.get('target_price', 'N/A')}")

    print("\n🤖 AI Analysis:")
    print("-" * 40)
    analysis = analyze_stock(data)
    print(analysis)


if __name__ == "__main__":
    main()
