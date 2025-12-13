import pytest

from src.category import Category
from src.product import Product



def test_category_init(category1, category2):
    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category1.products) == 2


def test_category_init_manual():
    p1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
    )
    p2 = Product(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
    )
    cat = Category("Смартфоны", "Описание категории", [p1, p2])

    assert cat.name == "Смартфоны"
    assert cat.description == "Описание категории"
    assert len(cat.products) == 2
    assert (
        cat.products_info[0]
        == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    )
    assert (
        cat.products_info[1]
        == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    )


def test_category_add_product():
    cat = Category("Смартфоны", "Описание категории")
    p = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    cat.add_product(p)

    assert len(cat.products) == 1
    assert (
        cat.products_info[0]
        == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    )


def test_category_counts():
    # Сбрасываем счетчики для теста
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
    )
    p2 = Product(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
    )
    cat1 = Category("Смартфоны", "Описание категории", [p1, p2])  # noqa: F841

    p3 = Product(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
    )
    cat2 = Category("Телевизоры", "Описание категории", [p3])  # noqa: F841

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_category_creation():
    product1 = Product("Smartphone1", "Описание", 100, 10)
    category = Category("Смартфоны", "Smartphones", [product1])

    assert category.name == "Смартфоны"
    assert len(category.products) == 1
    assert category.category_count == 1


def test_category_add_product():
    product1 = Product("Smartphone1", "Описание", 100, 10)
    product2 = Product("Smartphone2", "Описание", 200, 5)

    category = Category("Смартфоны", "Smartphones", [product1])
    category.add_product(product2)

    assert len(category.products) == 2

def reset_category_counters():
    Category.category_count = 0
    Category.product_count = 0