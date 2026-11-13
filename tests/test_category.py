from src.category import Category
from src.product import Product


def test_category_init(
    sample_category: Category, sample_product_1: Product
) -> None:
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == "Современные телефоны"
    expected_str = (
        "Samsung Galaxy S23, 80000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 95000.0 руб. Остаток: 10 шт.\n"
    )
    assert sample_category.products == expected_str


def test_category_add_product(
    sample_category: Category, sample_product_1: Product
) -> None:
    assert Category.product_count == 2
    new_prod = Product("Pixel 8", "Google", 65000.0, 4)
    sample_category.add_product(new_prod)

    assert Category.product_count == 3
    assert "Pixel 8, 65000.0 руб. Остаток: 4 шт.\n" in sample_category.products


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
