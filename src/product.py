class Product:
    name: str
    description: str
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.__price = 0
        self.price = price  # установка через сеттер

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Складывать можно только товары одного и того же класса.
        """
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных типов")

        return self.quantity + other.quantity

    @classmethod
    def new_product(cls, data: dict):
        return cls(**data)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value
