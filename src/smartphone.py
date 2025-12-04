from src.product import Product


class Smartphone(Product):
    def __init__(self, name, description, price, quantity,
                 efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Складывать можно только товары одного типа")
        return super().__add__(other)
