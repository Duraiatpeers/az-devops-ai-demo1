import pytest

from order_totals import LineItem, calculate_total


def test_calculates_total_without_discount():
    items = [LineItem(sku="SKU1", quantity=2, unit_price=10.00)]

    total = calculate_total(items, discount_code=None)

    assert total == 20.00


def test_zero_quantity_contributes_nothing():
    items = [LineItem(sku="SKU1", quantity=0, unit_price=10.00)]

    assert calculate_total(items) == 0.00


def test_zero_unit_price_contributes_nothing():
    items = [LineItem(sku="SKU1", quantity=3, unit_price=0.00)]

    assert calculate_total(items) == 0.00


def test_negative_quantity_raises_value_error():
    items = [LineItem(sku="SKU1", quantity=-2, unit_price=10.00)]

    with pytest.raises(ValueError):
        calculate_total(items)


def test_negative_unit_price_raises_value_error():
    items = [LineItem(sku="SKU1", quantity=2, unit_price=-10.00)]

    with pytest.raises(ValueError):
        calculate_total(items)


def test_negative_quantity_and_unit_price_raise_value_error():
    items = [LineItem(sku="SKU1", quantity=-2, unit_price=-10.00)]

    with pytest.raises(ValueError):
        calculate_total(items)


def test_total_rounds_fractional_unit_prices_to_two_decimal_places():
    items = [LineItem(sku="SKU1", quantity=3, unit_price=0.333)]

    assert calculate_total(items) == 1.00
