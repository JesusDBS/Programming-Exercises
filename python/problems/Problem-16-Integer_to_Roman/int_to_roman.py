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
            return self.__convert_digit(number=self)

        if len(str(self)) == 2:
            return self.__convert_2_digits_number(number=self)
            

        #     pass
        # Use divmod

        return False

    def __check_if_number_is_base(self, number=None):
        if not number:
            number = self
       
        if number in self.roman_numbers.keys():
            for _number in self.roman_numbers.keys():
                if _number == number:
                    return _number
        return False

    def __integer_to_string(self):
        number = str(self)
        return number
    
    def __convert_digit(self, number):
        if len(str(number)) == 1:
            if 1 < number < 5:
                if (number:=number // 1) <= 3:
                    return self.roman_numbers[1]*number
            
            if 5 < number < 9:
                if (number:=number % 5) <= 3:
                    return self.roman_numbers[5] + self.roman_numbers[1]*number

        return False
    
    def __convert_2_digits_number(self, number):
        #TODO: refactor this method

        if len(str(number)) == 2:
            quotient, remainder = divmod(number, 10)
            if 1 <= quotient < 4:
                if (number := self.__check_if_number_is_base(number=remainder)):
                    return self.roman_numbers[10]*quotient + self.roman_numbers[number]
                
                if not remainder:
                    return self.roman_numbers[10]*quotient
                
                return self.roman_numbers[10]*quotient + self.__convert_digit(remainder)
         
            if quotient == 4:
                fourty = self.roman_numbers[10] + self.roman_numbers[50]

                if (number := self.__check_if_number_is_base(number=remainder)):
                    return fourty + self.roman_numbers[number]
                
                if not remainder:
                    return fourty
                
                return fourty + self.__convert_digit(number=remainder)
            
            if 5 <= quotient < 10 and self <= 59:
                fifty = self.roman_numbers[50]
                
                if (number := self.__check_if_number_is_base(number=remainder)):
                    return fifty + self.roman_numbers[number]
                
                if not remainder:
                    return fifty
                
                return fifty + self.__convert_digit(number=remainder)
            
            if 60 <= self <= 99:
                quotient, remainder = divmod(number, 50)
                base = self.roman_numbers[50]

                if (num := remainder // 10) <= 3:
                    base += self.roman_numbers[10]*num
                
                else:
                    base = self.roman_numbers[10] + self.roman_numbers[100]

                if (resto:=remainder % 10) == 0:
                    return base
            
                if 1 <= resto <= 9:
                    if (number := self.__check_if_number_is_base(number=resto)):
                        return base + self.roman_numbers[number]
                    
                    return base + self.__convert_digit(resto) 
         
            
        return False

    

