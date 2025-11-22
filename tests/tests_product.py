from src.product import Product


def test_product_init(product1, product2):
    # Используем product1, а не несуществующую переменную product
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_new_product():
    data = {
        "name": "Яблоко",
        "description": "Красное и сладкое",
        "price": 80,
        "quantity": 15,
    }
    product = Product.new_product(data)
    assert product.name == "Яблоко"
    assert product.description == "Красное и сладкое"
    assert product.price == 80
    assert product.quantity == 15


def test_price_setter_valid():
    product = Product("Товар", "Описание", 100, 5)
    product.price = 150
    assert product.price == 150


def test_price_setter_invalid(capfd):
    product = Product("Товар", "Описание", 100, 5)
    product.price = -50
    out, _ = capfd.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in out
    assert product.price == 100  # цена не изменилась


def test_price_zero(capfd):
    product = Product("Товар", "Описание", 100, 5)
    product.price = 0
    out, _ = capfd.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in out
    assert product.price == 100
