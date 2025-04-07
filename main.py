
class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    category_count = 0  # Атрибут класса: количество категорий
    product_count = 0   # Атрибут класса: количество товаров

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        # Автоматическое обновление атрибутов класса
        Category.category_count += 1
        Category.product_count += len(products)
