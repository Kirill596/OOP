import unittest

from src.product import Product
from main import BaseProduct


class TestProduct(unittest.TestCase):
    def test_product_inheritance(self):
        """Проверяем, что Product наследуется от BaseProduct."""
        self.assertTrue(issubclass(Product, BaseProduct))

    def test_mixin_logging(self):
        """Проверяем, что миксин печатает сообщение при создании."""
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output

        product = Product("Тест", "Тест", 100, 5)
        self.assertIn("Создан объект класса Product", captured_output.getvalue())

        sys.stdout = sys.__stdout__  # Возвращаем stdout


if __name__ == "__main__":
    unittest.main()
