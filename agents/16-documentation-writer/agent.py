1. Module title and one-line description
2. Features list (bullet points)
3. Installation section
4. Quick Start with working code example
5. API Reference (each public function/class with parameters, return type, example)
6. Configuration (environment variables if any)
7. Error Handling section

Write in clear, developer-friendly markdown. Be specific and concrete."""

DOCSTRING_PROMPT = """Add comprehensive Google-style docstrings to every function and class that lacks them.

Format:
```
def function(param: type) -> return_type:
    \"\"\"One-line summary.

    Args:
        param: Description of parameter.

    Returns:
        Description of return value.

    Raises:
        ErrorType: When this error is raised.

    Example:
        >>> function(value)
        expected_output
    \"\"\"
```

Return the complete updated Python file with docstrings added."""


def generate_readme(code: str, filename: str) -> str:
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    structure = extract_structure(code)
    messages = [
        SystemMessage(content=README_PROMPT),
        HumanMessage(content=f"File: {filename}\n\nCode structure:\n{structure}\n\nFull code:\n```python\n{code[:3000]}\n```"),
    ]
    return llm.invoke(messages).content


def add_docstrings(code: str, filename: str) -> str:
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    messages = [
        SystemMessage(content=DOCSTRING_PROMPT),
