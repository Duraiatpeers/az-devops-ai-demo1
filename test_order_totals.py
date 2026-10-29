from order_totals import LineItem, calculate_total


def test_calculates_total_without_discount():
    items = [LineItem(sku="SKU1", quantity=2, unit_price=10.00)]

    total = calculate_total(items, discount_code=None)

    assert total == 20.00
