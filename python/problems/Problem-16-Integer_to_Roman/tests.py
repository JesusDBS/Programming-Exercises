import unittest
from int_to_roman import IntegerToRoman

class TestIntegerToRoman(unittest.TestCase):
    def setUp(self) -> None:
        self.int_to_roman = IntegerToRoman(10)
        return super().setUp()
    
    def tearDown(self) -> None:
        del self.int_to_roman
        return super().tearDown()
    
    def test_integer_to_roman_is_integer_instance(self):
        self.assertTrue(isinstance(self.int_to_roman, int))

    def test_check_convert_zero(self):
        zero = IntegerToRoman(0)
        self.assertEqual(zero.convert_to_roman(), 'N')

    def test_convert_to_roman_base_numbers(self):
        number = 'X'
        self.assertEqual(self.int_to_roman.convert_to_roman(), number)

    def test_convert_4_to_roman(self):
        four = IntegerToRoman(4)
        self.assertEqual(four.convert_to_roman(), 'IV')

    def test_convert_9_to_roman(self):
        nine = IntegerToRoman(9)
        self.assertEqual(nine.convert_to_roman(), 'IX')

    def test_convert_2_to_roman(self):
        two = IntegerToRoman(2)
        self.assertEqual(two.convert_to_roman(), 'II')

    def test_convert_3_to_roman(self):
        three = IntegerToRoman(3)
        self.assertEqual(three.convert_to_roman(), 'III')

    def test_convert_6_to_roman(self):
        six = IntegerToRoman(6)
        self.assertEqual(six.convert_to_roman(), 'VI')

    def test_convert_7_to_roman(self):
        seven = IntegerToRoman(7)
        self.assertEqual(seven.convert_to_roman(), 'VII')

    def test_convert_8_to_roman(self):
        eight = IntegerToRoman(8)
        self.assertEqual(eight.convert_to_roman(), 'VIII')


if __name__ == "__main__":
    unittest.main()