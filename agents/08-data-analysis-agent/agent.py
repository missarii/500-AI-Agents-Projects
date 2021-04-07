        rows.append({
            "date": d.isoformat(),
            "product": random.choice(products),
            "region": random.choice(regions),
            "quantity": random.randint(1, 20),
            "unit_price": round(random.uniform(50, 2000), 2),
            "revenue": 0,
        })

    df = pd.DataFrame(rows)
    df["revenue"] = df["quantity"] * df["unit_price"]
    df.to_csv(path, index=False)
    return df


def main():
    parser = argparse.ArgumentParser(description="Data Analysis Agent")
    parser.add_argument("--file", default="sample_data.csv", help="CSV or Excel file to analyze")
    parser.add_argument("--question", help="Single question (omit for interactive mode)")
    parser.add_argument(
        "--allow-dangerous-code",
        action="store_true",
        help="Required to let the pandas agent execute generated Python code locally",
    )
    args = parser.parse_args()

    if args.file == "sample_data.csv" and not os.path.exists("sample_data.csv"):
        print("🏗️  Creating sample sales dataset...")
        df = create_sample_data("sample_data.csv")
    else:
        ext = os.path.splitext(args.file)[1].lower()
        df = pd.read_excel(args.file) if ext in (".xlsx", ".xls") else pd.read_csv(args.file)

    print(f"\n📊 Loaded: {args.file} ({len(df)} rows × {len(df.columns)} columns)")
    print(f"📋 Columns: {', '.join(df.columns)}\n")

