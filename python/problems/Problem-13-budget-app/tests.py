import unittest
from budget_app import BudgetApp


class TestBudgetApp(unittest.TestCase):
    def setUp(self) -> None:
        self.snacks = BudgetApp('snacks', 100)
        self.food = BudgetApp('food', 500)
        return super().setUp()

    def test_display_budget(self):
        message = 'Your budget for snacks is 100 $'
        self.assertEqual(message, self.snacks.display_budget())

    def test_deposit_amount(self):
        result = 200
        self.snacks.deposit_amount(100)
        self.assertEqual(result, self.snacks.budget)

    def test_deposit_amount_type_error(self):
        self.assertRaises(TypeError, self.snacks.deposit_amount, 'HOLA')

    def test_deposit_amount_value_error_1(self):
        self.assertRaises(ValueError, self.snacks.deposit_amount, 0)

    def test_deposit_amount_value_error_2(self):
        self.assertRaises(ValueError, self.snacks.deposit_amount, -1)

    def test_withdraw_funds(self):
        result = 50
        self.snacks.withdraw_funds(50)
        self.assertEqual(result, self.snacks.budget)

    def test_withdraw_funds_type_error(self):
        self.assertRaises(TypeError, self.snacks.withdraw_funds, 'HOLA')

    def test_withdraw_funds_value_error_1(self):
        self.assertRaises(ValueError, self.snacks.withdraw_funds, 0)

    def test_withdraw_funds_value_error_2(self):
        self.assertRaises(ValueError, self.snacks.withdraw_funds, -1)

    def test_transfer_founds(self):
        self.snacks.transfer_founds(50, self.food)
        self.assertEqual(50, self.snacks.budget)
        self.assertEqual(550, self.food.budget)

    def test_transfer_founds_type_error(self):
        self.assertRaises(
            TypeError, self.snacks.transfer_founds, 'Hola', self.food)

    def test_transfer_founds_value_error_1(self):
        self.assertRaises(
            ValueError, self.snacks.transfer_founds, 0, self.food)

    def test_transfer_founds_value_error_2(self):
        self.assertRaises(
            ValueError, self.snacks.transfer_founds, -1, self.food)


if __name__ == '__main__':
    unittest.main()
