        else:
            self.items[name] = {"price": price, "quantity": quantity}

    def remove_item(self, name: str):
        if name not in self.items:
            raise KeyError(f"Item '{name}' not in cart")
        del self.items[name]

    def total(self) -> float:
        return sum(item["price"] * item["quantity"] for item in self.items.values())
'''


def generate_tests(code: str, filename: str = "module") -> str:
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    messages = [
        SystemMessage(content=TEST_PROMPT),
        HumanMessage(content=f"Generate tests for this Python code (from `{filename}`):\n\n```python\n{code}\n```"),
    ]
    response = llm.invoke(messages)
    return response.content


def main():
    parser = argparse.ArgumentParser(description="Unit Test Generator")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--file", help="Python file to generate tests for")
    group.add_argument("--code", help="Inline code to generate tests for")
    parser.add_argument("--output", help="Output file path (default: test_<name>.py)")
    args = parser.parse_args()

    if args.file:
