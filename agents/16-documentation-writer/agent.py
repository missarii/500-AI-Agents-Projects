        HumanMessage(content=f"Add docstrings to this Python file ({filename}):\n\n```python\n{code}\n```"),
    ]
    result = llm.invoke(messages).content
    # Clean markdown fences
    if "```python" in result:
        result = result.split("```python")[1].split("```")[0].strip()
    return result


SAMPLE_CODE = r'''
import hashlib
import re
from datetime import datetime


def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def hash_password(password: str, salt: str = "") -> str:
    combined = f"{password}{salt}"
    return hashlib.sha256(combined.encode()).hexdigest()


def parse_date(date_string: str) -> datetime:
    formats = ["%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y", "%Y%m%d"]
    for fmt in formats:
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue
    raise ValueError(f"Unable to parse date: {date_string}")


class UserValidator:
    MIN_PASSWORD_LENGTH = 8

    def validate_username(self, username: str) -> tuple[bool, str]:
        if len(username) < 3:
            return False, "Username too short"
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            return False, "Only letters, numbers, underscores allowed"
        return True, ""

    def validate_password(self, password: str) -> tuple[bool, str]:
        if len(password) < self.MIN_PASSWORD_LENGTH:
            return False, f"Password must be at least {self.MIN_PASSWORD_LENGTH} characters"
