import pytest

from app.pricing import calculate_total


def test_regular_order_has_no_discount():
    assert calculate_total(10.0, 3) == 30.0


def test_bulk_discount_starts_at_ten_units():
    assert calculate_total(10.0, 10) == 90.0


def test_bulk_discount_applies_above_threshold():
    assert calculate_total(10.0, 12) == 108.0


def test_quantity_must_be_positive():
    with pytest.raises(ValueError):
        calculate_total(10.0, 0)
