from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """
    Абстрактный базовый класс для всех продуктов.
    Содержит общие атрибуты и контракт поведения.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        """Строковое представление продукта"""
        pass

    @abstractmethod
    def __add__(self, other):
        """Сложение продуктов"""
        pass
