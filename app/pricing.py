def calculate_total(unit_price: float, quantity: int) -> float:
    """Calculate an order total with a 10% bulk discount from 10 units."""
    if unit_price < 0:
        raise ValueError("unit_price must be non-negative")
    if quantity <= 0:
        raise ValueError("quantity must be greater than zero")

    subtotal = unit_price * quantity
    if quantity > 10:
        subtotal *= 0.90

    return round(subtotal, 2)
