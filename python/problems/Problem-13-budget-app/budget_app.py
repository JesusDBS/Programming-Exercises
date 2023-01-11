#!/usr/bin/env python3
"""
Author: Jesús David Briceño <jesusbingucv@gmail.com>
Purpose: A simple budget class.
"""
# ---------------------------------------------------
# Budget App:
# Create a Budget class that can instantiate objects based on different budget categories like food, clothing,
# and entertainment. These objects should allow for depositing and withdrawing funds from each category,
# as well computing category balances and transferring balance amounts between categories.
# ---------------------------------------------------


class BudgetApp:
    """
    A simple class to do your budgets.
    """
    currency = '$'

    def __init__(self, category: str, budget=0):
        self.category = category
        self.budget = budget

    def display_budget(self):
        message = f'Your budget for {self.category} is {self.budget} {self.currency}'
        print(message)
        return message
