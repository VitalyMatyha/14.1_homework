from src.smartphone import Smartphone

def test_smartphone_creation():
    s = Smartphone("Samsung Galaxy S23", "Описание", 180000, 5, 95.5, "S23", 256, "Серый")
    assert s.name == "Samsung Galaxy S23"
    assert s.model == "S23"
    assert s.price == 180000
    assert s.quantity == 5
    assert s.efficiency == 95.5

def test_smartphone_addition():
    s1 = Smartphone("A", "D", 100, 10, 90, "M1", 128, "Black")
    s2 = Smartphone("B", "D", 200, 2, 88, "M2", 256, "White")
    assert s1 + s2 == 1000 + 400
