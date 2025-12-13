import pytest
from src.product import Product
from src.category import Category

def test_main_creation_and_category():
    # Создание продуктов
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)

    # Проверка атрибутов
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product2.price == 210000.0
    assert product3.quantity == 14

    # Создание категорий
    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    # Проверка категорий
    assert category1.name == "Смартфоны"
    assert len(category1.products) == 3
    assert category1.product_count >= 3
    assert Category.category_count >= 2

    assert category2.name == "Телевизоры"
    assert len(category2.products) == 1
    assert category2.products[0].name == "55\" QLED 4K"

    # Проверка добавления продукта
    product5 = Product("Test Product", "Description", 1000.0, 2)
    category1.add_product(product5)
    assert len(category1.products) == 4
    assert category1.products[-1].name == "Test Product"

    # Проверка ошибки при добавлении не продукта
    with pytest.raises(TypeError):
        category1.add_product("Not a product")
