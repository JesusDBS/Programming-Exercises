import unittest
from budget_app import BudgetApp


class TestBudgetApp(unittest.TestCase):
    def test_display_budget(self):
        snacks = BudgetApp('snacks', 100)
        message = 'Your budget for snacks is 100 $'
        self.assertEqual(message, snacks.display_budget())


if __name__ == '__main__':
    unittest.main()
