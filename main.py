from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, description, price, quantity):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать продукты разных типов")
        return self.price * self.quantity + other.price * other.quantity

class Smartphone(Product):
    def __init__(self, name, description, price, quantity, 
                 efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity,
                 country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

class Category:
    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []

    def add_product(self, product):
        if not isinstance(product, (Product, Smartphone, LawnGrass)):
            raise TypeError("Можно добавлять только продукты или их наследники")
        self.__products.append(product)

    def average_price(self):
        if not self.__products:
            return 0
        return sum(p.price for p in self.__products) / len(self.__products)

    @property
    def products(self):
        return "\n".join(str(p) for p in self.__products)
