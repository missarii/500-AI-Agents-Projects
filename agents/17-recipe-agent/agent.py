      "cook_time": "X minutes",
      "servings": N,
      "ingredients_needed": ["ingredient (amount)"],
      "missing_ingredients": ["optional additions"],
      "instructions": ["Step 1: ...", "Step 2: ..."],
      "nutrition_per_serving": {"calories": N, "protein": "Xg", "carbs": "Xg", "fat": "Xg"},
      "tips": "Chef's tip"
    }
  ],
  "recommended": "Recipe Name (best match)"
}
Return only valid JSON."""


def parse_json_response(text: str) -> dict:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
        cleaned = re.sub(r"\s*```$", "", cleaned)
    match = re.search(r"\{.*\}", cleaned, re.DOTALL)
    if match:
        cleaned = match.group(0)
    return json.loads(cleaned)


def get_recipes(ingredients: list[str], diet: str, time_limit: int, servings: int) -> dict:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

    constraints = []
    if diet:
        constraints.append(f"Dietary restriction: {diet}")
