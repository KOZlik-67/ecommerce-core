from src.category import Category
from src.product import Product


def test_category_init(
    sample_category: Category, sample_product_1: Product
) -> None:
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == "Современные телефоны"
    assert len(sample_category.products) == 2
    assert sample_category.products[0] == sample_product_1


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
