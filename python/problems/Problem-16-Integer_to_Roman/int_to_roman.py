#-----------------------------------------
#Integer to Roman
# Write a Python class to convert an integer to a Roman numeral.
#-----------------------------------------

class IntegerToRoman(int):
    """
    Simple class for convert integer numbers to roman base numbers.
    """
    roman_numbers = {
        0: 'N',
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
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
        
        if number == 0 and type(number) == int:
            return self.roman_numbers[number]
        
        if len(str(self)) == 1:
            return self.__convert_digit()

        return False

    def __check_if_number_is_base(self):
        if self in self.roman_numbers.keys():
            for number in self.roman_numbers.keys():
                if number == self:
                    return number
        return False

    def __integer_to_string(self):
        number = str(self)
        return number
    
    def __convert_digit(self):
        number = self
        if len(str(number)) == 1:
            if 1 < number < 5:
                if (number:=number // 1) <= 3:
                    return self.roman_numbers[1]*number
            
            if 5 < number < 9:
                if (number:=number % 5) <= 3:
                    return self.roman_numbers[5] + self.roman_numbers[1]*number

        return False

        

    

