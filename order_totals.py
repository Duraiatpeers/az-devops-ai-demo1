from dataclasses import dataclass


@dataclass
class LineItem:
    sku: str
    quantity: int
    unit_price: float


DISCOUNT_RATE = 0.10


def calculate_total(items: list[LineItem], discount_code: str | None = None) -> float:
    subtotal = 0.0
    for item in items:
        if item.quantity < 0:
            raise ValueError("quantity cannot be negative")
        if item.unit_price < 0:
            raise ValueError("unit_price cannot be negative")
        subtotal += item.unit_price * item.quantity

    if discount_code == "SAVE10":
        subtotal -= subtotal * DISCOUNT_RATE

    return round(subtotal, 2)
