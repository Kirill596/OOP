# src/product.py
from main import BaseProduct


class LoggingMixin:
    """Mixin class that logs object creation."""

    def __init__(self, *args, **kwargs):
        print(f"Создан объект класса {self.__class__.__name__}")
        super().__init__(*args, **kwargs)


class Product(LoggingMixin, BaseProduct):
    """Класс продукта, наследуемый от BaseProduct с добавлением логирования."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name, description, price, quantity)

    def __add__(self, other):
        """Складывает продукты одного типа по количеству, проверяя тип и цену."""
        if not isinstance(other, self.__class__):
            raise TypeError("Можно складывать только продукты одного класса")
        if self.price != other.price:
            raise ValueError("Нельзя складывать продукты с разной ценой")
        return self.quantity + other.quantity
