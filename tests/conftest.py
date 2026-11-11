from typing import Generator
import pytest
from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_category_counts() -> Generator[None, None, None]:
    """Сбрасывает счетчики категорий перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0
    yield
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def sample_product_1() -> Product:
    return Product("Samsung Galaxy S23", "Флагман", 80000.0, 5)


@pytest.fixture
def sample_product_2() -> Product:
    return Product("Iphone 15", "Смартфон Apple", 95000.0, 10)


@pytest.fixture
def sample_category(
    sample_product_1: Product, sample_product_2: Product
) -> Category:
    return Category(
        name="Смартфоны",
        description="Современные телефоны",
        products=[sample_product_1, sample_product_2],
    )
