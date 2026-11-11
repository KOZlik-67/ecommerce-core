from typing import List
from src.product import Product


class Category:
    """Класс для представления категории товаров."""

    category_count: int = 0
    product_count: int = 0

    name: str
    description: str
    products: List[Product]

    def __init__(
        self, name: str, description: str, products: List[Product]
    ) -> None:
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)
