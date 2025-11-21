from src.product import Product
from src.category import Category


if __name__ == "__main__":
    # Создание продуктов
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создание категории
    category1 = Category(
        "Смартфоны",
        "Современные смартфоны для любых задач"
    )

    # Добавление продуктов в категорию
    category1.add_product(product1)
    category1.add_product(product2)
    category1.add_product(product3)

    print("Товары категории после добавления:")
    print(category1.products)

    # Добавление ещё одного товара
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)

    print("\nТовары категории после добавления телевизора:")
    print(category1.products)

    print("\nОбщее количество товаров во всех категориях:")
    print(Category.product_count)

    # Создание товара через classmethod
    new_product = Product.new_product({
        "name": "Наушники Sony WH-1000XM5",
        "description": "Беспроводные, шумоподавление",
        "price": 39000.0,
        "quantity": 4
    })

    print("\nСоздан новый товар через classmethod:")
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    # Демонстрация работы проверок
    print("\nИзменение цены товара:")
    new_product.price = 8000
    print("Новая цена:", new_product.price)

    # Некорректная цена (с отловом)
    try:
        new_product.price = -100
    except ValueError as e:
        print("Ошибка:", e)
