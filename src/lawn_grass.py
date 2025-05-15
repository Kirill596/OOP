# src/lawn_grass.py
from src.product import Product


class LawnGrass(Product):
    def __init__(self, *, country: str, germination_period: int,
                 color: str, **base):
        super().__init__(**base)
        self.country = country
        self.germination_period = germination_period
        self.color = color
