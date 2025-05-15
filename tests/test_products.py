# tests/test_products.py
import pytest
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


@pytest.fixture
def phone():
    return Smartphone(
        name="iPhone",
        description="Apple",
        price=100_000,
        quantity=3,
        efficiency="A16",
        model="15 Pro",
        memory=256,
        color="black",
    )


@pytest.fixture
def grass():
    return LawnGrass(
        name="Greeny",
        description="Газон",
        price=2000,
        quantity=5,
        country="NL",
        germination_period=14,
        color="green",
    )


def test_add_same_class(phone):
    another = Smartphone(
        name="iPhone",
        description="Apple",
        price=100_000,
        quantity=2,
        efficiency="A16",
        model="15 Pro",
        memory=256,
        color="black",
    )
    assert phone + another == 5


def test_add_different_classes(phone, grass):
    with pytest.raises(TypeError):
        _ = phone + grass


def test_category_rejects_str():
    from src.category import Category
    cat = Category("Полка")
    with pytest.raises(TypeError):
        cat.add_product("не товар")  # type: ignore[arg-type]
