from typing import Iterator, List
from src.product import Product


class ZeroQuantityError(Exception):
    """Исключение при попытке добавить товар с нулевым количеством."""

    def __init__(
        self,
        message: str = "Товар с нулевым количеством не может быть добавлен",
    ) -> None:
        super().__init__(message)


class Category:
    """Класс для представления категории товаров."""

    category_count: int = 0
    product_count: int = 0

    name: str
    description: str
    __products: List[Product]

    def __init__(
        self, name: str, description: str, products: List[Product]
    ) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты Product и его наследников"
            )
        try:
            if product.quantity == 0:
                raise ZeroQuantityError()
        except ZeroQuantityError as err:
            print(err)
        else:
            self.__products.append(product)
            Category.product_count += 1
            print("Товар успешно добавлен")
        finally:
            print("Обработка добавления товара завершена")

    def middle_price(self) -> float:
        try:
            return sum(p.price for p in self.__products) / len(
                self.__products
            )
        except ZeroDivisionError:
            return 0

    @property
    def products(self) -> str:
        return "".join(f"{str(p)}\n" for p in self.__products)

    @property
    def products_list(self) -> List[Product]:
        """Возвращает исходный список товаров для работы итератора."""
        return self.__products


class CategoryIterator:
    """Вспомогательный класс для перебора товаров категории в цикле."""

    def __init__(self, category: Category) -> None:
        self.category = category
        self.index = 0

    def __iter__(self) -> Iterator[Product]:
        self.index = 0
        return self

    def __next__(self) -> Product:
        products = self.category.products_list
        if self.index < len(products):
            product = products[self.index]
            self.index += 1
            return product
        raise StopIteration
