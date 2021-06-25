
def main():
    parser = argparse.ArgumentParser(description="Recipe Recommendation Agent")
    parser.add_argument("--ingredients", default="chicken breast, garlic, lemon, olive oil, rosemary, potatoes", help="Comma-separated ingredients")
    parser.add_argument("--diet", default="", help="Dietary restriction (vegan, vegetarian, gluten-free, keto, etc.)")
    parser.add_argument("--time", type=int, default=0, help="Max cooking time in minutes")
    parser.add_argument("--servings", type=int, default=2, help="Number of servings")
    args = parser.parse_args()

    ingredients = [i.strip() for i in args.ingredients.split(",")]
    print(f"\n🥘 Finding recipes with: {', '.join(ingredients)}")
    if args.diet:
        print(f"🥗 Diet: {args.diet}")
    if args.time:
        print(f"⏱️  Max time: {args.time} minutes")

    result = get_recipes(ingredients, args.diet, args.time, args.servings)

    print("\n" + "=" * 60)
    recipes = result.get("recipes", [])
    recommended = result.get("recommended") or (recipes[0].get("name", "N/A") if recipes else "N/A")
    print("✅ RECOMMENDED:", recommended)
    print("=" * 60)

    for recipe in recipes:
        display_recipe(recipe)
        print("\n" + "-" * 40)


if __name__ == "__main__":
    main()
