from src.base_product import BaseProduct
from src.mixins import CreationLogMixin


class Product(CreationLogMixin, BaseProduct):
    def __init__(self, name, description, price, quantity):
        self.__price = 0
        super().__init__(name, description, price, quantity)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"name='{self.name}', "
            f"description='{self.description}', "
            f"price={self.price}, "
            f"quantity={self.quantity})"
        )

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать продукты разных классов")
        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

