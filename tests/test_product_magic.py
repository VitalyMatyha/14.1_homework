from src.product import Product
from src.category import Category


def test_product_str():
    p = Product("Test", "Desc", 80, 15)
    assert str(p) == "Test, 80 руб. Остаток: 15 шт."


def test_category_str():
    p1 = Product("A", "D", 100, 10)
    p2 = Product("B", "D", 200, 5)
    cat = Category("Phones", "Desc", [p1, p2])

    assert str(cat) == "Phones, количество продуктов: 15 шт."


def test_product_add():
    p1 = Product("A", "D", 100, 10)  # 1000
    p2 = Product("B", "D", 200, 2)   # 400

    assert p1 + p2 == 1400


def test_product_add_invalid():
    p = Product("A", "D", 100, 10)

    try:
        p + 10
    except TypeError:
        assert True
    else:
        assert False
