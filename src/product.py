from typing import Any, Dict, List, Optional


class Product:
    """Класс для представления товара."""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            answer = input(
                "Вы уверены, что хотите понизить цену? (y/n): "
            ).strip().lower()
            if answer != "y":
                return

        self.__price = new_price

    @classmethod
    def new_product(
        cls,
        product_data: Dict[str, Any],
        products_list: Optional[List["Product"]] = None,
    ) -> "Product":
        name = str(product_data["name"])
        description = str(product_data["description"])
        price = float(product_data["price"])
        quantity = int(product_data["quantity"])

        if products_list:
            for existing in products_list:
                if existing.name.lower() == name.lower():
                    existing.quantity += quantity
                    if price > existing.price:
                        existing.price = price
                    return existing

        return cls(
            name=name,
            description=description,
            price=price,
            quantity=quantity,
        )
