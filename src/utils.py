import json
import os
from typing import Any, Dict, List
from src.category import Category
from src.product import Product


def load_data_from_json(file_path: str) -> List[Category]:
    """Считывает JSON-файл и формирует список объектов Category."""
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        data: List[Dict[str, Any]] = json.load(f)

    categories: List[Category] = []
    for category_dict in data:
        products: List[Product] = []
        for prod_dict in category_dict.get("products", []):
            products.append(
                Product(
                    name=prod_dict["name"],
                    description=prod_dict["description"],
                    price=float(prod_dict["price"]),
                    quantity=int(prod_dict["quantity"]),
                )
            )
        categories.append(
            Category(
                name=category_dict["name"],
                description=category_dict["description"],
                products=products,
            )
        )
    return categories
