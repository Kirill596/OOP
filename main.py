class Product:
    """Базовый класс продукта"""
    total_products = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.total_products += 1

    @classmethod
    def new_product(cls, product_data):
        """Создает новый продукт из словаря"""
        return cls(
            name=product_data['name'],
            description=product_data.get('description', ''),
            price=product_data['price'],
            quantity=product_data.get('quantity', 0)
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена введена некорректная")
        elif new_price < self.__price:
            confirmation = input("Вы уверены, что хотите снизить цену? (y/n): ")
            if confirmation.lower() == 'y':
                self.__price = new_price
        else:
            self.__price = new_price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать продукты разных типов")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    """Класс смартфона (наследник Product)"""

    def __init__(self, name, description, price, quantity,
                 efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс газонной травы (наследник Product)"""

    def __init__(self, name, description, price, quantity,
                 country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    """Класс категории товаров"""
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.total_categories += 1

    def add_product(self, product):
        """Добавление продукта с проверкой типа"""
        if not isinstance(product, (Product, Smartphone, LawnGrass)):
            raise TypeError("Можно добавлять только продукты или их наследники")

        # Проверка на дубликат
        existing_product = next((p for p in self.__products if p.name == product.name), None)
        if existing_product:
            existing_product.quantity += product.quantity
            if existing_product.price != product.price:
                existing_product.price = product.price
        else:
            self.__products.append(product)
            Category.total_unique_products += 1

    @property
    def products(self):
        """Геттер для вывода информации о продуктах"""
        return "\n".join(str(product) for product in self.__products) + "\n"

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
