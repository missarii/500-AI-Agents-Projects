    if time_limit:
        constraints.append(f"Max total time: {time_limit} minutes")
    if servings:
        constraints.append(f"Servings needed: {servings}")

    messages = [
        SystemMessage(content=RECIPE_PROMPT),
        HumanMessage(content=f"Available ingredients: {', '.join(ingredients)}\n\nConstraints:\n{chr(10).join(constraints) if constraints else 'None'}"),
    ]

    response = llm.invoke(messages)
    return parse_json_response(response.content)


def display_recipe(recipe: dict):
    print(f"\n🍽️  {recipe.get('name', 'Recipe')} ({recipe.get('cuisine', 'N/A')})")
    print(f"⏱️  Prep: {recipe.get('prep_time', 'N/A')} | Cook: {recipe.get('cook_time', 'N/A')} | Difficulty: {recipe.get('difficulty', 'N/A')}")
    print(f"👥 Serves: {recipe.get('servings', 'N/A')}")
    print(f"\n📝 Ingredients:")
    for ing in recipe.get("ingredients_needed", []):
        print(f"  • {ing}")
    if recipe.get("missing_ingredients"):
        print(f"\n➕ Optional additions: {', '.join(recipe['missing_ingredients'])}")
    print(f"\n👨‍🍳 Instructions:")
    for i, step in enumerate(recipe.get("instructions", []), 1):
        print(f"  {i}. {step}")
    n = recipe.get("nutrition_per_serving", {})
    if n:
        print(f"\n🥗 Nutrition: {n.get('calories', '?')} cal | Protein: {n.get('protein', '?')} | Carbs: {n.get('carbs', '?')} | Fat: {n.get('fat', '?')}")
    if recipe.get("tips"):
        print(f"\n💡 Chef's tip: {recipe['tips']}")

