#-----------------------------------------
#Integer to Roman
# Write a Python class to convert an integer to a Roman numeral.
#-----------------------------------------

class IntegerToRoman(int):
    """
    Simple class for convert integer numbers to roman base numbers
    """
    roman_numbers = {
        0: 'N',
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }

    def convert_to_roman(self):
        """
        Converts integer number to roman
        """
        if (number := self.__check_if_number_is_base()):
            return self.roman_numbers[number]
        return False

    def __check_if_number_is_base(self):
        if self in self.roman_numbers.keys():
            for number in self.roman_numbers.keys():
                if number == self:
                    return number
        return False

