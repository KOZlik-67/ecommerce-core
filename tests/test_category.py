import pytest
from src.category import Category, CategoryIterator
from src.product import Product, Smartphone


def test_category_init(sample_category: Category) -> None:
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == "Современные телефоны"
    expected_str = (
        "Samsung Galaxy S23, 80000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 95000.0 руб. Остаток: 10 шт.\n"
    )
    assert sample_category.products == expected_str


def test_category_str(sample_category: Category) -> None:
    assert str(sample_category) == "Смартфоны, количество продуктов: 15 шт."


def test_category_middle_price(sample_category: Category) -> None:
    assert sample_category.middle_price() == 87500.0

    empty_category = Category("Пустая категория", "Нет товаров", [])
    assert empty_category.middle_price() == 0


def test_category_add_product(sample_category: Category) -> None:
    assert Category.product_count == 2
    new_prod = Product("Pixel 8", "Google", 65000.0, 4)
    sample_category.add_product(new_prod)

    assert Category.product_count == 3
    expected = "Pixel 8, 65000.0 руб. Остаток: 4 шт.\n"
    assert expected in sample_category.products


def test_category_add_zero_quantity_product(
    sample_category: Category, sample_product_1: Product, capsys: object
) -> None:
    sample_product_1.quantity = 0
    sample_category.add_product(sample_product_1)
    captured = capsys.readouterr()  # type: ignore[attr-defined]
    assert "Товар с нулевым количеством не может быть добавлен" in captured.out
    assert "Обработка добавления товара завершена" in captured.out


def test_category_and_product_counts(
    sample_product_1: Product, sample_product_2: Product
) -> None:
    assert Category.category_count == 0
    assert Category.product_count == 0

    cat1 = Category("Категория 1", "Описание 1", [sample_product_1])
    assert Category.category_count == 1
    assert Category.product_count == 1
    assert cat1.category_count == 1

    Category(
        "Категория 2",
        "Описание 2",
        [sample_product_1, sample_product_2],
    )
    assert Category.category_count == 2
    assert Category.product_count == 3


def test_category_iterator(
    sample_category: Category,
    sample_product_1: Product,
    sample_product_2: Product,
) -> None:
    iterator = CategoryIterator(sample_category)
    items = list(iterator)
    assert items == [sample_product_1, sample_product_2]


def test_add_invalid_product_error(sample_category: Category) -> None:
    with pytest.raises(TypeError):
        sample_category.add_product("Не продукт")  # type: ignore[arg-type]

    phone = Smartphone(
        "Samsung", "Флагман", 100000.0, 2, 95.5, "S23", 256, "Черный"
    )
    sample_category.add_product(phone)
    expected = "Samsung, 100000.0 руб. Остаток: 2 шт.\n"
    assert expected in sample_category.products
