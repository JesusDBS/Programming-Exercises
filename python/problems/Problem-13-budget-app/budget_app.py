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
    instances = list()

    def __init__(self, category: str, budget=0):
        self.category = category
        self.budget = budget
        self.__class__.instances.append(self)

    def display_budget(self):
        message = f'Your budget for {self.category} is {self.budget} {self.currency}'
        print(message)
        return message

    @staticmethod
    def check_vals(amount):
        if not (isinstance(amount, int) or isinstance(amount, float)):
            raise TypeError

        if amount <= 0:
            raise ValueError

    def deposit_amount(self, amount: int):
        self.check_vals(amount)
        self.budget += amount
        self.display_budget()

    def withdraw_funds(self, amount: int):
        self.check_vals(amount)
        self.budget -= amount
        self.display_budget()

    def transfer_founds(self, amount: int, another_category):
        self.check_vals(amount)
        self.withdraw_funds(amount)
        another_category.deposit_amount(amount)

    @classmethod
    def get_total_spend(cls):
        spend_by_category = list(map(lambda c: c.budget, cls.instances))
        cls.total_spend = sum(spend_by_category)

    @classmethod
    def get_spend_by_category(cls):
        cls.get_total_spend()
        spend_by_category = dict()

        for category in cls.instances:
            spend_by_category[category.category] = category.budget / \
                cls.total_spend * 100

        cls.spend_by_category = spend_by_category

        for key, val in spend_by_category.items():
            print(f'{key}: {val:.2f} %')
