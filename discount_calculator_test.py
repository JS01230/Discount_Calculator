#discount calculator test
import unittest
from discount_calculator import DiscountCalculator

def setUp(self):
		self.calc = DiscountCalculator()

class DiscountCalculatorTests(unittest.TestCase):
	def test_ten_percent_discount(self):
		discount_calculator = DiscountCalculator()
		result = discount_calculator.calculate(100,10,'percent')
		self.assertEqual(10.0, result)