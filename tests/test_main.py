import pytest
from main import Product, Smartphone, LawnGrass, Category


def test_smartphone_creation():
    phone = Smartphone("iPhone", "Smart", 100000, 10, "A15", "13", 256, "Black")
    assert phone.name == "iPhone"
    assert phone.memory == 256


def test_lawn_grass_creation():
    grass = LawnGrass("Grass", "Lawn", 500, 100, "Russia", "14d", "Green")
    assert grass.country == "Russia"
    assert grass.germination_period == "14d"


def test_add_same_type():
    p1 = Product("Prod1", "Desc", 100, 2)
    p2 = Product("Prod2", "Desc", 200, 3)
    assert p1 + p2 == 800


def test_add_different_types():
    p = Product("Prod", "Desc", 100, 1)
    phone = Smartphone("Phone", "Smart", 1000, 1, "A", "M", 128, "Black")
    with pytest.raises(TypeError):
        p + phone


def test_add_non_product():
    cat = Category("Cat", "Desc")
    with pytest.raises(TypeError):
        cat.add_product("Not a product")


def test_average_price():
    cat = Category("Cat", "Desc", [
        Product("P1", "D", 100, 1),
        Product("P2", "D", 200, 1)
    ])
    assert cat.average_price() == 150


def test_zero_quantity():
    with pytest.raises(ValueError):
        Product("P", "D", 100, 0)
