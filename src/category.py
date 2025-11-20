from src.product import Product

class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0


    def __init__(self, name, description ):
        self.name = name
        self.description = description
        self.__products = [] #всегда пустой приватный
        Category.category_count += 1


    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return self.__products.copy()

    @property
    def products_info(self):
        """Возвращает список товаров в виде строк."""
        info_list = []
        for product in self.__products:
            info_list.append(
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            )
        return info_list








