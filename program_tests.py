import unittest
import math
from program import add, subtract, multiply, divide, modulus, factorial, power, sqrt

class TestCalculatorFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, 0), "Помилка! Ділення на нуль.")

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(10, 0), "Помилка! Ділення на нуль.")

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(-3), "Помилка! Факторіал визначений тільки для цілих невід’ємних чисел.")
        self.assertEqual(factorial(4.5), "Помилка! Факторіал визначений тільки для цілих невід’ємних чисел.")

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_sqrt(self):
        self.assertEqual(sqrt(9), 3)
        self.assertEqual(sqrt(-1), "Помилка! Квадратний корінь з від’ємного числа неможливий.")

if __name__ == "__main__":
    unittest.main()
