import pytest
from main import Product, Category


def test_product_zero_quantity():
    """Тест создания продукта с нулевым количеством"""
    with pytest.raises(ValueError) as excinfo:
        Product("Телефон", "Смартфон", 10000, 0)
    assert "Товар с нулевым количеством не может быть добавлен" in str(excinfo.value)


def test_product_normal_creation():
    """Тест нормального создания продукта"""
    product = Product("Телефон", "Смартфон", 10000, 5)
    assert product.name == "Телефон"
    assert product.quantity == 5


def test_category_average_price_empty():
    """Тест средней цены для пустой категории"""
    category = Category("Электроника", "Техника")
    assert category.average_price() == 0


def test_category_average_price_with_products():
    """Тест средней цены для категории с товарами"""
    category = Category("Электроника", "Техника")
    category.add_product(Product("Телефон", "Смартфон", 10000, 5))
    category.add_product(Product("Ноутбук", "Игровой", 50000, 3))
    assert category.average_price() == 30000


def test_category_average_price_single_product():
    """Тест средней цены для категории с одним товаром"""
    category = Category("Электроника", "Техника")
    category.add_product(Product("Телефон", "Смартфон", 10000, 5))
    assert category.average_price() == 10000
