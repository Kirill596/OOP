# main.py
class BaseProduct:
    """Базовый класс для всех продуктов."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self) -> str:  # не обязательно для тестов, но полезно
        return (f"{self.__class__.__name__}("
                f"name={self.name!r}, description={self.description!r}, "
                f"price={self.price!r}, quantity={self.quantity!r})")
