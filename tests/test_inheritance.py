import pytest
from src.product import Product
from src.category import Category
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass

# -----------------------------
# Тесты для Smartphone
# -----------------------------
def test_smartphone_init():
    s = Smartphone("S1", "Desc", 100, 10, 95, "M1", 128, "Black")
    assert s.name == "S1"
    assert s.description == "Desc"
    assert s.price == 100
    assert s.quantity == 10
    assert s.efficiency == 95
    assert s.model == "M1"
    assert s.memory == 128
    assert s.color == "Black"

def test_smartphone_str():
    s = Smartphone("S1", "Desc", 100, 10, 95, "M1", 128, "Black")
    assert str(s) == "S1, 100 руб. Остаток: 10 шт."

def test_add_same_class_smartphone():
    s1 = Smartphone("S1", "D", 100, 10, 90, "M1", 128, "Black")
    s2 = Smartphone("S2", "D", 200, 2, 88, "M2", 256, "White")
    assert s1 + s2 == 100*10 + 200*2

def test_add_different_class_smartphone_typeerror():
    s = Smartphone("S1", "D", 100, 10, 90, "M1", 128, "Black")
    g = LawnGrass("G1", "D", 50, 5, "RU", "7 дней", "Green")
    with pytest.raises(TypeError):
        s + g

# -----------------------------
# Тесты для LawnGrass
# -----------------------------
def test_lawngrass_init():
    g = LawnGrass("G1", "Desc", 50, 5, "RU", "7 дней", "Green")
    assert g.name == "G1"
    assert g.description == "Desc"
    assert g.price == 50
    assert g.quantity == 5
    assert g.country == "RU"
    assert g.germination_period == "7 дней"
    assert g.color == "Green"

def test_lawngrass_str():
    g = LawnGrass("G1", "Desc", 50, 5, "RU", "7 дней", "Green")
    assert str(g) == "G1, 50 руб. Остаток: 5 шт."

def test_add_same_class_lawngrass():
    g1 = LawnGrass("G1", "D", 100, 10, "RU", "7 дней", "Green")
    g2 = LawnGrass("G2", "D", 200, 2, "US", "5 дней", "Dark")
    assert g1 + g2 == 100*10 + 200*2

def test_add_different_class_lawngrass_typeerror():
    g = LawnGrass("G1", "D", 100, 10, "RU", "7 дней", "Green")
    s = Smartphone("S1", "D", 50, 5, 90, "M1", 128, "Black")
    with pytest.raises(TypeError):
        g + s

# -----------------------------
# Тесты Category с наследниками
# -----------------------------
def test_category_add_product_inheritance():
    cat = Category("Test", "Desc")
    s = Smartphone("S1", "D", 100, 10, 90, "M1", 128, "Black")
    g = LawnGrass("G1", "D", 50, 5, "RU", "7 дней", "Green")
    p = Product("P1", "D", 20, 2)

    # Можно добавлять Product и наследников
    cat.add_product(s)
    cat.add_product(g)
    cat.add_product(p)

    assert len(cat.products) == 3
    assert cat.products[0] == s
    assert cat.products[1] == g
    assert cat.products[2] == p

def test_category_add_product_invalid():
    cat = Category("Test", "Desc")
    with pytest.raises(TypeError):
        cat.add_product("Not a product")
