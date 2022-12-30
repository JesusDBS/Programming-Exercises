import re
from .calculator import Calculator


class InputValuesError(Exception):
    """Check if input is correct
    """

    def __init__(self, values, message="Please type your input as follows: first number + sing operation + second number."):
        self.values = values
        self.message = message

        super().__init__(self.message)

    def __str__(self):
        return f"{self.values}! --> {self.message}"


class UserInterface:
    """A Simple class to make user interface.
    """
    user_input = ''
    buffer = ''

    @classmethod
    def get_input(cls, user_input):

        if not isinstance(user_input, str):
            raise TypeError

        if len(user_input.split()) > 3:
            raise InputValuesError(user_input)

        if len(user_input.split()) <= 2:
            raise InputValuesError(user_input)

        cls.user_input = user_input

    @classmethod
    def clen_buffer(cls):
        cls.buffer = ''

    @classmethod
    def validate_input(cls):
        pattern = re.compile('^[\d|\.|\,]+')
        input_parts = cls.user_input.split()

        values = []
        for el in input_parts:
            if pattern.findall(el):
                if not bool(cls.buffer):
                    cls.buffer = el.replace(',', '.')
                    continue

                if cls.buffer:
                    cls.buffer += el
                    continue

            if cls.buffer.endswith('.'):
                cls.buffer = cls.buffer + '0'
            values.append(cls.buffer)
            cls.clen_buffer()
            values.append(el)
            if len(values) == 3:
                break

        if bool(cls.buffer):
            if cls.buffer.endswith('.'):
                cls.buffer = cls.buffer + '0'
            values.append(cls.buffer)
            cls.clen_buffer()
        return values

    @classmethod
    def do_operation(cls, values):
        operation = values[1]
        first_num = float(values[0])
        second_num = float(values[2])

        if operation == '+':
            cls.buffer = Calculator.suma(first_num, second_num)
            return True

        if operation == '-':
            cls.buffer = Calculator.substraction(first_num, second_num)
            return True

        if operation == '/':
            cls.buffer = Calculator.division(first_num, second_num)
            return True

        if operation == '^':
            cls.buffer = Calculator.exponentiation(first_num, second_num)
            return True

        if operation == 'x':
            cls.buffer = Calculator.multiply(first_num, second_num)
            return True
