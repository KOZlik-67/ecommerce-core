from src.product import Product


def test_product_init(sample_product_1: Product) -> None:
    assert sample_product_1.name == "Samsung Galaxy S23"
    assert sample_product_1.description == "Флагман"
    assert sample_product_1.price == 80000.0
    assert sample_product_1.quantity == 5
