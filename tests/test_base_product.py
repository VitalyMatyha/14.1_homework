import pytest
from src.base_product import BaseProduct
from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass

def test_baseproduct_instantiation_raises():
    # Нельзя создавать объект абстрактного класса напрямую
    with pytest.raises(TypeError):
        BaseProduct("Name", "Description", 100, 1)

def test_product_inherits_baseproduct():
    p = Product("Product1", "Описание", 100, 2)
    assert isinstance(p, BaseProduct)
    assert p.name == "Product1"
    assert p.description == "Описание"
    assert p.price == 100
    assert p.quantity == 2

def test_smartphone_inherits_baseproduct():
    s = Smartphone("Phone1", "Описание", 200, 3, 90, "M1", 128, "Black")
    assert isinstance(s, BaseProduct)
    assert s.name == "Phone1"
    assert s.description == "Описание"
    assert s.price == 200
    assert s.quantity == 3
    assert s.efficiency == 90
    assert s.model == "M1"
    assert s.memory == 128
    assert s.color == "Black"

def test_lawngrass_inherits_baseproduct():
    g = LawnGrass("Grass1", "Описание", 50, 5, "RU", "7 дней", "Green")
    assert isinstance(g, BaseProduct)
    assert g.name == "Grass1"
    assert g.description == "Описание"
    assert g.price == 50
    assert g.quantity == 5
    assert g.country == "RU"
    assert g.germination_period == "7 дней"
    assert g.color == "Green"


def test_baseproduct_methods_via_product():
    p = Product("Test", "Desc", 100, 5)
    assert p.name == "Test"
    assert p.description == "Desc"
    assert p.price == 100
    assert p.quantity == 5

def test_baseproduct_methods_via_smartphone():
    s = Smartphone("X", "Desc", 200, 2, 90, "Model", 128, "Black")
    assert s.name == "X"
    assert s.price == 200

def test_baseproduct_methods_via_lawngrass():
    g = LawnGrass("Grass", "Desc", 50, 10, "RU", "7 дней", "Green")
    assert g.name == "Grass"
    assert g.price == 50