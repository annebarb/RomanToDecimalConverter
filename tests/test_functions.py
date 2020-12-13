import unittest
from functions import roman_to_decimal as rtd


class TestRomanToDecimal(unittest.TestCase):

    # decimal_to_roman

    def test_decimal_to_roman(self):
        converter = rtd.decimal_to_roman(1)
        self.assertEqual(converter, "I")

    def test_decimal_to_roman(self):
        converter = rtd.decimal_to_roman(18)
        self.assertEqual(converter, "XVIII")

    def test_decimal_to_roman(self):
        converter = rtd.decimal_to_roman(3999)
        self.assertEqual(converter, "MMMCMXCIX")

    def test_decimal_to_roman(self):
        converter = rtd.decimal_to_roman(9)
        self.assertNotEqual(converter, "VIIII")

    def test_decimal_to_roman(self):
        self.assertRaises(TypeError, rtd.decimal_to_roman, "X")

    # roman_to_decimal

    def test_roman_to_decimal(self):
        converter = rtd.roman_to_decimal("IV")
        self.assertEqual(converter, 4)

    def test_roman_to_decimal(self):
        converter = rtd.roman_to_decimal("XXXV")
        self.assertEqual(converter, 35)

    def test_roman_to_decimal(self):
        converter = rtd.roman_to_decimal("MMMCMXCIX")
        self.assertEqual(converter, 3999)

    def test_roman_to_decimal(self):
        self.assertRaises(TypeError, rtd.roman_to_decimal, 1212)

    def test_roman_to_decimal(self):
        self.assertRaises(ValueError, rtd.roman_to_decimal, "IXX")

    def test_roman_to_decimal(self):
        self.assertRaises(ValueError, rtd.roman_to_decimal, "MMMCMXCXI")

    def test_roman_to_decimal(self):
        self.assertRaises(ValueError, rtd.roman_to_decimal, "VIV")

    def test_roman_to_decimal(self):
        self.assertRaises(ValueError, rtd.roman_to_decimal, "IVIV")
