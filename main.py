from src.category import Category
from src.product import Product

if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi 14", "128GB, Черный", 75000.0, 15)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации",
        [product1, product2, product3],
    )

    print(category1.name)
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор для дома",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(Category.category_count)
    print(Category.product_count)
