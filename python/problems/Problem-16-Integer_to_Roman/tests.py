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

    def test_convert_to_roman_base_numbers(self):
        number = 'X'
        self.assertEqual(self.int_to_roman.convert_to_roman(), number)


if __name__ == "__main__":
    unittest.main()