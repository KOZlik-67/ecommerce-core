from pathlib import Path
from src.utils import load_data_from_json


def test_load_data_from_json(tmp_path: Path) -> None:
    json_file = tmp_path / "test_products.json"
    json_file.write_text(
        """[
            {
                "name": "Телевизоры",
                "description": "Современные экраны",
                "products": [
                    {
                        "name": "LG OLED",
                        "description": "55 дюймов",
                        "price": 120000.0,
                        "quantity": 2
                    }
                ]
            }
        ]""",
        encoding="utf-8",
    )

    categories = load_data_from_json(str(json_file))
    assert len(categories) == 1
    assert categories[0].name == "Телевизоры"
    assert len(categories[0].products) == 1
    assert categories[0].products[0].name == "LG OLED"


def test_load_data_non_existent_file() -> None:
    categories = load_data_from_json("unknown_file.json")
    assert categories == []
