#-----------------------------------------
#Integer to Roman
# Write a Python class to convert an integer to a Roman numeral.
#-----------------------------------------

class IntegerToRoman(int):
    """
    Simple class for convert integer numbers to roman base numbers.
    """
    roman_numbers = [
    ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
    ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
    ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
    ]

    def convert_to_roman(self):
        """
        Converts integer number to roman
        """
        roman = ''
        num = self
        if num == 0:
            return 'N'
        
        for _roman, _number in self.roman_numbers:
            while num >= _number:
                roman += _roman
                num -= _number
        return roman