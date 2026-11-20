from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class BaseProduct(ABC):
    """Базовый абстрактный класс для всех продуктов."""

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other: Any) -> float:
        pass

    @classmethod
    @abstractmethod
    def new_product(
            cls,
            product_data: Dict[str, Any],
            products_list: Optional[List[Any]] = None,
    ) -> Any:
        pass


class PrintMixin:
    """Миксин для логирования создания экземпляра класса в консоль."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        print(repr(self))
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        attrs = ", ".join(repr(arg) for arg in self.__dict__.values())
        return f"{self.__class__.__name__}({attrs})"


class Product(PrintMixin, BaseProduct):
    """Базовый класс для представления товара."""

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
        super().__init__()

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return (self.__price * self.quantity) + (
                other.__price * other.quantity
        )

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            answer = (
                input("Вы уверены, что хотите понизить цену? (y/n): ")
                .strip()
                .lower()
            )
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


class Smartphone(Product):
    """Класс для представления товара категории Смартфон."""

    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            efficiency: float,
            model: str,
            memory: int,
            color: str,
    ) -> None:
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)


class LawnGrass(Product):
    """Класс для представления товара категории Трава газонная."""

    country: str
    germination_period: str
    color: str

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            country: str,
            germination_period: str,
            color: str,
    ) -> None:
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)
