import pytest
from src.main import __name__  # noqa
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass
from src.category import Category

def test_smartphone_creation():
    s = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый", 180000, 5, 95.5, "S23 Ultra", 256, "Серый")
    assert s.name == "Samsung Galaxy S23 Ultra"
    assert s.description == "256GB, Серый"
    assert s.price == 180000
    assert s.quantity == 5
    assert s.efficiency == 95.5
    assert s.model == "S23 Ultra"
    assert s.memory == 256
    assert s.color == "Серый"

def test_lawngrass_creation():
    g = LawnGrass("Газонная трава", "Элитная", 500, 20, "Россия", "7 дней", "Зеленый")
    assert g.name == "Газонная трава"
    assert g.description == "Элитная"
    assert g.price == 500
    assert g.quantity == 20
    assert g.country == "Россия"
    assert g.germination_period == "7 дней"
    assert g.color == "Зеленый"

def test_add_same_class_sum():
    s1 = Smartphone("A", "D", 100, 10, 90, "M1", 128, "Black")
    s2 = Smartphone("B", "D", 200, 2, 88, "M2", 256, "White")
    assert s1 + s2 == 1000 + 400

    g1 = LawnGrass("A", "D", 100, 10, "RU", "7 дней", "Green")
    g2 = LawnGrass("B", "D", 200, 2, "US", "5 дней", "Dark")
    assert g1 + g2 == 1000 + 400

def test_add_different_class_raises():
    s = Smartphone("A", "D", 100, 10, 90, "M1", 128, "Black")
    g = LawnGrass("B", "D", 200, 2, "US", "5 дней", "Dark")
    with pytest.raises(TypeError):
        _ = s + g

def test_category_add_and_count():
    s1 = Smartphone("A", "D", 100, 10, 90, "M1", 128, "Black")
    s2 = Smartphone("B", "D", 200, 2, 88, "M2", 256, "White")
    g1 = LawnGrass("A", "D", 100, 10, "RU", "7 дней", "Green")

    cat = Category("Test Cat", "Описание")
    cat.add_product(s1)
    cat.add_product(s2)
    cat.add_product(g1)

    assert len(cat.products) == 3
    assert Category.product_count >= 3  # учитывая, что счетчик глобальный

def test_category_add_invalid_raises():
    cat = Category("Test Cat", "Описание")
    with pytest.raises(TypeError):
        cat.add_product("Invalid Object")



