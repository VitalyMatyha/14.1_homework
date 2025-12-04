import pytest
from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass
from src.category import Category


def test_smartphone_init():
    s = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "Описание",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый"
    )
    assert s.name == "Samsung Galaxy S23 Ultra"
    assert s.description == "Описание"
    assert s.price == 180000.0
    assert s.quantity == 5
    assert s.efficiency == 95.5
    assert s.model == "S23 Ultra"
    assert s.memory == 256
    assert s.color == "Серый"


def test_lawngrass_init():
    g = LawnGrass(
        "Газонная трава",
        "Описание",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый"
    )
    assert g.name == "Газонная трава"
    assert g.description == "Описание"
    assert g.price == 500.0
    assert g.quantity == 20
    assert g.country == "Россия"
    assert g.germination_period == "7 дней"
    assert g.color == "Зеленый"


def test_add_same_class_smartphone():
    s1 = Smartphone("A", "D", 100, 10, 90, "M1", 128, "Black")
    s2 = Smartphone("B", "D", 200, 2, 88, "M2", 256, "White")

    assert s1 + s2 == 1000 + 400


def test_add_same_class_lawngrass():
    g1 = LawnGrass("A", "D", 100, 10, "RU", "7 дней", "Green")
    g2 = LawnGrass("B", "D", 200, 2, "US", "5 дней", "Dark")

    assert g1 + g2 == 1000 + 400


def test_add_different_classes_error():
    s = Smartphone("A", "D", 100, 10, 90, "M", 128, "Black")
    g = LawnGrass("B", "D", 200, 2, "RU", "7 дней", "Green")

    with pytest.raises(TypeError):
        s + g


def test_add_product_accepts_only_products():
    cat = Category("Test", "Desc")
    s = Smartphone("A", "D", 100, 5, 90, "M", 128, "Black")

    cat.add_product(s)
    assert len(cat.products) == 1

    with pytest.raises(TypeError):
        cat.add_product("string")  # not a product
