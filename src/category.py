from src.product import Product   # путь поправьте под проект


class Category:
    def __init__(self, name: str) -> None:
        self.name = name
        self._products: list[Product] = []

    def add_product(self, product: Product) -> None:
        """Принимаем **только** объекты-товары."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавить только экземпляр Product (или его подкласса)")
        self._products.append(product)
