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

    def test_convert_11_to_roman(self):
        number = IntegerToRoman(11)
        self.assertEqual(number.convert_to_roman(), 'XI')

    def test_convert_13_to_roman(self):
        number = IntegerToRoman(13)
        self.assertEqual(number.convert_to_roman(), 'XIII')

    def test_convert_14_to_roman(self):
        number = IntegerToRoman(14)
        self.assertEqual(number.convert_to_roman(), 'XIV')

    def test_convert_17_to_roman(self):
        number = IntegerToRoman(17)
        self.assertEqual(number.convert_to_roman(), 'XVII')

    def test_convert_18_to_roman(self):
        number = IntegerToRoman(18)
        self.assertEqual(number.convert_to_roman(), 'XVIII')

    def test_convert_19_to_roman(self):
        number = IntegerToRoman(19)
        self.assertEqual(number.convert_to_roman(), 'XIX')

    def test_convert_20_to_roman(self):
        number = IntegerToRoman(20)
        self.assertEqual(number.convert_to_roman(), 'XX')

    def test_convert_21_to_roman(self):
        number = IntegerToRoman(21)
        self.assertEqual(number.convert_to_roman(), 'XXI')

    def test_convert_24_to_roman(self):
        number = IntegerToRoman(24)
        self.assertEqual(number.convert_to_roman(), 'XXIV')

    def test_convert_27_to_roman(self):
        number = IntegerToRoman(27)
        self.assertEqual(number.convert_to_roman(), 'XXVII')

    def test_convert_29_to_roman(self):
        number = IntegerToRoman(29)
        self.assertEqual(number.convert_to_roman(), 'XXIX')

    def test_convert_30_to_roman(self):
        number = IntegerToRoman(30)
        self.assertEqual(number.convert_to_roman(), 'XXX')

    def test_convert_33_to_roman(self):
        number = IntegerToRoman(33)
        self.assertEqual(number.convert_to_roman(), 'XXXIII')

    def test_convert_39_to_roman(self):
        number = IntegerToRoman(39)
        self.assertEqual(number.convert_to_roman(), 'XXXIX')

    def test_convert_40_to_roman(self):
        number = IntegerToRoman(40)
        self.assertEqual(number.convert_to_roman(), 'XL')

    def test_convert_41_to_roman(self):
        number = IntegerToRoman(41)
        self.assertEqual(number.convert_to_roman(), 'XLI')

    def test_convert_43_to_roman(self):
        number = IntegerToRoman(43)
        self.assertEqual(number.convert_to_roman(), 'XLIII')

    def test_convert_44_to_roman(self):
        number = IntegerToRoman(44)
        self.assertEqual(number.convert_to_roman(), 'XLIV')

    def test_convert_49_to_roman(self):
        number = IntegerToRoman(49)
        self.assertEqual(number.convert_to_roman(), 'XLIX')

    def test_convert_50_to_roman(self):
        number = IntegerToRoman(50)
        self.assertEqual(number.convert_to_roman(), 'L')

    def test_convert_51_to_roman(self):
        number = IntegerToRoman(51)
        self.assertEqual(number.convert_to_roman(), 'LI')

    def test_convert_58_to_roman(self):
        number = IntegerToRoman(58)
        self.assertEqual(number.convert_to_roman(), 'LVIII')

    def test_convert_59_to_roman(self):
        number = IntegerToRoman(59)
        self.assertEqual(number.convert_to_roman(), 'LIX')

    def test_convert_60_to_roman(self):
        number = IntegerToRoman(60)
        self.assertEqual(number.convert_to_roman(), 'LX')

    def test_convert_70_to_roman(self):
        number = IntegerToRoman(70)
        self.assertEqual(number.convert_to_roman(), 'LXX')

    def test_convert_80_to_roman(self):
        number = IntegerToRoman(80)
        self.assertEqual(number.convert_to_roman(), 'LXXX')

    def test_convert_90_to_roman(self):
        number = IntegerToRoman(90)
        self.assertEqual(number.convert_to_roman(), 'XC')

    def test_convert_91_to_roman(self):
        number = IntegerToRoman(91)
        self.assertEqual(number.convert_to_roman(), 'XCI')

    def test_convert_93_to_roman(self):
        number = IntegerToRoman(93)
        self.assertEqual(number.convert_to_roman(), 'XCIII')

    def test_convert_92_to_roman(self):
        number = IntegerToRoman(92)
        self.assertEqual(number.convert_to_roman(), 'XCII')

    def test_convert_94_to_roman(self):
        number = IntegerToRoman(94)
        self.assertEqual(number.convert_to_roman(), 'XCIV')

    def test_convert_96_to_roman(self):
        number = IntegerToRoman(96)
        self.assertEqual(number.convert_to_roman(), 'XCVI')

    def test_convert_97_to_roman(self):
        number = IntegerToRoman(97)
        self.assertEqual(number.convert_to_roman(), 'XCVII')

    def test_convert_98_to_roman(self):
        number = IntegerToRoman(98)
        self.assertEqual(number.convert_to_roman(), 'XCVIII')

    def test_convert_99_to_roman(self):
        number = IntegerToRoman(99)
        self.assertEqual(number.convert_to_roman(), 'XCIX')

    def test_convert_100_to_roman(self):
        number = IntegerToRoman(100)
        self.assertEqual(number.convert_to_roman(), 'C')




if __name__ == "__main__":
    unittest.main()