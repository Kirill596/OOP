import pytest
from main import BaseProduct, Product, Smartphone, LawnGrass, LoggingMixin


def test_base_product_is_abstract():
    """Проверка, что BaseProduct - абстрактный класс"""
    with pytest.raises(TypeError):
        BaseProduct("Test", "Test", 100, 1)


def test_product_inheritance():
    """Проверка наследования Product"""
    assert issubclass(Product, (BaseProduct, LoggingMixin))


def test_smartphone_creation(capsys):
    """Тест создания смартфона и логирования"""
    _ = Smartphone(  # Используем _ для неиспользуемой переменной
        "iPhone", "Smartphone", 100000, 10,
        "A15", "13 Pro", 256, "Black"
    )
    captured = capsys.readouterr()
    assert "Создан объект класса Smartphone" in captured.out
    assert "iPhone" in captured.out


def test_lawn_grass_creation(capsys):
    """Тест создания газонной травы и логирования"""
    _ = LawnGrass(  # Используем _ для неиспользуемой переменной
        "Grass", "Lawn", 500, 100,
        "Russia", "14 days", "Green"
    )
    captured = capsys.readouterr()
    assert "Создан объект класса LawnGrass" in captured.out
    assert "Grass" in captured.out


def test_product_methods():
    """Тест методов продукта"""
    product = Product("Test", "Test", 100, 5)
    assert str(product) == "Test, 100 руб. Остаток: 5 шт."
    product2 = Product("Test", "Test", 100, 3)
    assert product + product2 == 800
