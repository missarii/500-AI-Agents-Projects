
Output ONLY the complete test file content, ready to run with `pytest`."""

SAMPLE_CODE = '''
def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate discounted price."""
    if price < 0:
        raise ValueError("Price cannot be negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - discount_percent / 100)


def find_longest_word(text: str) -> str:
    """Find the longest word in a text string."""
    if not text or not text.strip():
        return ""
    words = text.split()
    return max(words, key=len)


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name: str, price: float, quantity: int = 1):
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 1:
            raise ValueError("Quantity must be at least 1")
        if name in self.items:
            self.items[name]["quantity"] += quantity
