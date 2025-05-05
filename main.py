from abc import ABC, abstractmethod


class LoggingMixin:
    """Миксин для логирования создания объектов"""
    def __init__(self, *args, **kwargs):
        print(f"Создан объект класса {self.__class__.__name__} с параметрами:")
        print(f"Атрибуты: {args}")
        print(f"Ключевые атрибуты: {kwargs}")
        super().__init__(*args, **kwargs)


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов"""
    @abstractmethod
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class Product(LoggingMixin, BaseProduct):
    """Класс продукта с миксином и наследованием от абстрактного класса"""
    def __init__(self, name, description, price, quantity):
        super().__init__(name=name, description=description, 
                        price=price, quantity=quantity)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать продукты разных типов")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    """Класс смартфона"""
    def __init__(self, name, description, price, quantity, 
                 efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс газонной травы"""
    def __init__(self, name, description, price, quantity,
                 country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
