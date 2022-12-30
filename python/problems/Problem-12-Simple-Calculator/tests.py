import unittest
from app.calculator import Calculator
from app.calculator import NumberValuesError
from app.user_interface import UserInterface
from app.user_interface import InputValuesError


class TestCalculator(unittest.TestCase):
    """A Simple class to test calculator.
    """

    def setUp(self) -> None:
        Calculator.buffer = ''
        return super().setUp()

    def test_sum(self):
        result = Calculator.suma(1, 2)
        self.assertEqual(result, 3)

    def test_sum_return_none(self):
        result = Calculator.suma()
        self.assertIsNone(result)

    def test_substract(self):
        result = Calculator.substraction(4, 2, 1)
        self.assertEqual(result, 1)

    def test_sub_return_none(self):
        result = Calculator.substraction()
        self.assertIsNone(result)

    def test_division(self):
        result = Calculator.division(16, 2, 2)
        self.assertEqual(result, 4)

    def test_div_return_none(self):
        result = Calculator.division()
        self.assertIsNone(result)

    def test_exp(self):
        result = Calculator.exponentiation(2, 2, 2)
        self.assertEqual(result, 16)

    def test_exp_return_none(self):
        result = Calculator.exponentiation()
        self.assertIsNone(result)

    def test_mul(self):
        result = Calculator.multiply(5, 5)
        self.assertEqual(result, 25)

    def test_mul_return_none(self):
        result = Calculator.multiply()
        self.assertIsNone(result)

    def test_buffer(self):
        resut = Calculator.suma(1, 2)
        buffer = Calculator.buffer
        self.assertEqual(resut, buffer)

    def test_sum_using_buffer(self):
        Calculator.suma(1, 1)
        result = Calculator.suma(1)
        self.assertEqual(result, 3)

    def test_sub_using_buffer(self):
        Calculator.suma(1, 1)
        result = Calculator.substraction(1)
        self.assertEqual(result, 1)

    def test_div_using_buffer(self):
        Calculator.suma(1, 1)
        result = Calculator.division(2)
        self.assertEqual(result, 1)

    def test_exp_using_buffer(self):
        Calculator.suma(1, 1)
        result = Calculator.exponentiation(3)
        self.assertEqual(result, 8)

    def test_mul_using_buffer(self):
        Calculator.suma(1, 1)
        result = Calculator.multiply(3)
        self.assertEqual(result, 6)

    def test_sum_num_exception(self):
        self.assertRaises(NumberValuesError, Calculator.suma, 1)

    def test_sub_num_exception(self):
        self.assertRaises(NumberValuesError, Calculator.substraction, 1)

    def test_div_num_exception(self):
        self.assertRaises(NumberValuesError, Calculator.division, 1)

    def test_exp_num_exception(self):
        self.assertRaises(NumberValuesError, Calculator.exponentiation, 1)

    def test_mul_num_exception(self):
        self.assertRaises(NumberValuesError, Calculator.multiply, 1)

    def test_sum_type_exception(self):
        self.assertRaises(TypeError, Calculator.suma, '1', '2')

    def test_sub_type_exception(self):
        self.assertRaises(TypeError, Calculator.substraction, '1', '2')

    def test_div_type_exception(self):
        self.assertRaises(TypeError, Calculator.division, '1', '2')

    def test_exp_type_exception(self):
        self.assertRaises(TypeError, Calculator.exponentiation, '1', '2')

    def test_mul_type_exception(self):
        self.assertRaises(TypeError, Calculator.multiply, '1', '2')

    def test_div_zero_div_exception(self):
        self.assertRaises(ZeroDivisionError, Calculator.division, 1, 0)

    def test_clear_buffer(self):
        Calculator.suma(1, 1)
        Calculator.clear_buffer()
        self.assertEqual(Calculator.buffer, '')


class TestUserInterface(unittest.TestCase):
    """A Simple class to test user interface.
    """

    def setUp(self) -> None:
        UserInterface.user_input = ''
        UserInterface.buffer = ''
        return super().setUp()

    def test_input_type_exception(self):
        self.assertRaises(TypeError, UserInterface.get_input, 10)

    def test_validate_input_1(self):
        UserInterface.get_input('12 + 3.5 ')
        result = UserInterface.validate_input()
        self.assertEqual(result, ['12', '+', '3.5'])

    def test_input_vaidate_exception_1(self):
        self.assertRaises(InputValuesError,
                          UserInterface.get_input, '12 + 3.5 + 8 9')

    def test_input_vaidate_exception_2(self):
        self.assertRaises(InputValuesError,
                          UserInterface.get_input, '1 2 + 3.5 + 8 9')

    def test_input_vaidate_exception_3(self):
        self.assertRaises(InputValuesError,
                          UserInterface.get_input, '1235+7')

    def test_sum_UI(self):
        UserInterface.get_input('1 + 1')
        values = UserInterface.validate_input()
        UserInterface.do_operation(values)
        self.assertEqual(UserInterface.buffer, float(2))

    def test_sub_UI(self):
        UserInterface.get_input('1 - 1')
        values = UserInterface.validate_input()
        UserInterface.do_operation(values)
        self.assertEqual(UserInterface.buffer, float(0))

    def test_div_UI(self):
        UserInterface.get_input('4 / 2')
        values = UserInterface.validate_input()
        UserInterface.do_operation(values)
        self.assertEqual(UserInterface.buffer, float(2))

    def test_sum_UI(self):
        UserInterface.get_input('2 ^ 3')
        values = UserInterface.validate_input()
        UserInterface.do_operation(values)
        self.assertEqual(UserInterface.buffer, float(8))

    def test_mul_UI(self):
        UserInterface.get_input('2 x 3')
        values = UserInterface.validate_input()
        UserInterface.do_operation(values)
        self.assertEqual(UserInterface.buffer, float(6))


if __name__ == "__main__":
    unittest.main()
