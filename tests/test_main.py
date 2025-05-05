import pytest
from main import Product, Smartphone, LawnGrass, Category


@pytest.fixture
def sample_product():
    return Product("Телефон", "Смартфон", 10000, 5)


@pytest.fixture
def sample_smartphone():
    return Smartphone(
        "iPhone", "Флагман", 100000, 10,
        "A15", "13 Pro", 256, "Graphite"
    )


@pytest.fixture
def sample_lawn_grass():
    return LawnGrass(
        "Трава", "Для газона", 500, 100,
        "Россия", "14 дней", "Зеленая"
    )


@pytest.fixture
def sample_category():
    return Category("Электроника", "Технические устройства")


def test_product_creation(sample_product):
    assert sample_product.name == "Телефон"
    assert sample_product.description == "Смартфон"
    assert sample_product.price == 10000
    assert sample_product.quantity == 5


def test_smartphone_creation(sample_smartphone):
    assert sample_smartphone.efficiency == "A15"
    assert sample_smartphone.model == "13 Pro"
    assert sample_smartphone.memory == 256
    assert sample_smartphone.color == "Graphite"


def test_lawn_grass_creation(sample_lawn_grass):
    assert sample_lawn_grass.country == "Россия"
    assert sample_lawn_grass.germination_period == "14 дней"
    assert sample_lawn_grass.color == "Зеленая"


def test_add_different_types(
        sample_category,
        sample_smartphone,
        sample_lawn_grass):
    sample_category.add_product(sample_smartphone)
    sample_category.add_product(sample_lawn_grass)
    assert len(sample_category._Category__products) == 2


def test_add_invalid_type(sample_category):
    with pytest.raises(TypeError):
        sample_category.add_product("Не продукт")


def test_add_same_type_products(sample_product):
    product1 = Product("Ноутбук", "Игровой", 50000, 3)
    product2 = Product("Ноутбук", "Игровой", 45000, 2)
    total = (product1.price * product1.quantity +
             product2.price * product2.quantity)
    assert product1 + product2 == total


def test_add_different_type_products(
        sample_smartphone,
        sample_lawn_grass):
    with pytest.raises(TypeError):
        sample_smartphone + sample_lawn_grass


def test_price_reduction_confirmation(sample_product, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "n")
    sample_product.price = 8000
    assert sample_product.price == 10000

    monkeypatch.setattr('builtins.input', lambda _: "y")
    sample_product.price = 8000
    assert sample_product.price == 8000


def test_category_products_property(sample_category, sample_product):
    sample_category.add_product(sample_product)
    assert "Телефон" in sample_category.products
