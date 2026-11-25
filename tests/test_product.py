from unittest.mock import patch
import pytest
from src.product import BaseProduct, LawnGrass, PrintMixin, Product, Smartphone


def test_product_init(sample_product_1: Product) -> None:
    assert sample_product_1.name == "Samsung Galaxy S23"
    assert sample_product_1.description == "Флагман"
    assert sample_product_1.price == 80000.0
    assert sample_product_1.quantity == 5


def test_product_zero_quantity_error() -> None:
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Бракованный товар", "Описание", 1000.0, 0)


def test_product_str(sample_product_1: Product) -> None:
    expected = "Samsung Galaxy S23, 80000.0 руб. Остаток: 5 шт."
    assert str(sample_product_1) == expected


def test_product_add(
    sample_product_1: Product, sample_product_2: Product
) -> None:
    assert sample_product_1 + sample_product_2 == 1350000.0

    with pytest.raises(TypeError):
        _ = sample_product_1 + 100  # type: ignore[operator]


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


def test_smartphone_init() -> None:
    phone = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    assert phone.name == "Samsung Galaxy S23 Ultra"
    assert phone.efficiency == 95.5
    assert phone.model == "S23 Ultra"
    assert phone.memory == 256
    assert phone.color == "Серый"


def test_lawn_grass_init() -> None:
    grass = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    assert grass.name == "Газонная трава"
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_add_different_classes_error() -> None:
    phone1 = Smartphone(
        "Samsung", "Флагман", 100000.0, 2, 95.5, "S23", 256, "Черный"
    )
    phone2 = Smartphone(
        "Iphone", "Apple", 120000.0, 3, 98.0, "15", 512, "Серый"
    )
    grass = LawnGrass(
        "Трава", "Газонная", 500.0, 10, "Россия", "7 дней", "Зеленый"
    )

    assert phone1 + phone2 == 560000.0

    with pytest.raises(TypeError):
        _ = phone1 + grass


def test_base_product_and_mixin(capsys: object) -> None:
    assert issubclass(Product, BaseProduct)
    assert issubclass(Product, PrintMixin)

    Product("Тестовый товар", "Описание", 1000.0, 3)
    captured = capsys.readouterr()  # type: ignore[attr-defined]
    assert (
        "Product('Тестовый товар', 'Описание', 1000.0, 3)" in captured.out
    )
