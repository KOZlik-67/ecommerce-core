from unittest.mock import patch
from src.product import Product


def test_product_init(sample_product_1: Product) -> None:
    assert sample_product_1.name == "Samsung Galaxy S23"
    assert sample_product_1.description == "Флагман"
    assert sample_product_1.price == 80000.0
    assert sample_product_1.quantity == 5


def test_product_price_setter(
    sample_product_1: Product, capsys: object
) -> None:
    sample_product_1.price = 0
    captured = capsys.readouterr()  # type: ignore[attr-defined]
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product_1.price == 80000.0

    sample_product_1.price = -500
    assert sample_product_1.price == 80000.0

    sample_product_1.price = 90000.0
    assert sample_product_1.price == 90000.0


def test_product_price_decrease_confirm(sample_product_1: Product) -> None:
    with patch("builtins.input", return_value="n"):
        sample_product_1.price = 70000.0
    assert sample_product_1.price == 80000.0

    with patch("builtins.input", return_value="y"):
        sample_product_1.price = 70000.0
    assert sample_product_1.price == 70000.0


def test_new_product(sample_product_1: Product) -> None:
    data = {
        "name": "Xiaomi 14",
        "description": "Новый смартфон",
        "price": 60000.0,
        "quantity": 7,
    }
    prod = Product.new_product(data)
    assert prod.name == "Xiaomi 14"
    assert prod.price == 60000.0
    assert prod.quantity == 7

    dup_data = {
        "name": "Samsung Galaxy S23",
        "description": "Флагман",
        "price": 85000.0,
        "quantity": 3,
    }
    updated = Product.new_product(dup_data, [sample_product_1])
    assert updated is sample_product_1
    assert sample_product_1.quantity == 8
    assert sample_product_1.price == 85000.0
