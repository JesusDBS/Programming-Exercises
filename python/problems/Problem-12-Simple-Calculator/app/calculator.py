from functools import reduce


class NumberValuesError(Exception):
    """Check if there is more than one number
    """

    def __init__(self, values, message="You need more than one number to use this operation."):
        self.values = values
        self.message = message

        super().__init__(self.message)

    def __str__(self):
        return f"{self.values}! --> {self.message}"


class Calculator:
    """A Simple class to make aritmetics calculations.
    """

    buffer = ''

    @staticmethod
    def _args_to_values(args, buffer):
        values = []
        for el in args:
            if isinstance(el, int) or isinstance(el, float):
                values.append(el)
            else:
                raise TypeError

        if len(values) < 2 and isinstance(buffer, str):
            raise NumberValuesError(values)

        if len(values) < 2 and (isinstance(buffer, int) or isinstance(buffer, float)):
            values.append(buffer)
            values.reverse()

        return values

    @classmethod
    def suma(cls, *args):
        """
        Documentation here
        """
        if not bool(args):
            return None

        values = cls._args_to_values(args, cls.buffer)

        result = sum(values)
        cls.buffer = result
        return result

    @classmethod
    def substraction(cls, *args):
        """
        Documentation here
        """
        def substract(x, y):
            return x-y

        if not bool(args):
            return None

        values = cls._args_to_values(args, cls.buffer)

        result = reduce(substract, values)
        cls.buffer = result
        return result

    @classmethod
    def division(cls, *args):
        """
        Documentation here
        """
        def divide(x, y):
            return x/y

        if not bool(args):
            return None

        values = cls._args_to_values(args, cls.buffer)
        try:
            result = reduce(divide, values)
            cls.buffer = result
        except ZeroDivisionError as err:
            raise err
        return result

    @classmethod
    def multiply(cls, *args):
        """
        Documentation here
        """
        def mul(x, y):
            return x*y

        if not bool(args):
            return None

        values = cls._args_to_values(args, cls.buffer)

        result = reduce(mul, values)
        cls.buffer = result
        return result

    @classmethod
    def exponentiation(cls, *args):
        """
        Documentation here
        """
        def power(x, y):
            return x**y

        if not bool(args):
            return None

        values = cls._args_to_values(args, cls.buffer)

        result = reduce(power, values)
        cls.buffer = result
        return result

    @classmethod
    def clear_buffer(cls):
        cls.buffer = ''
