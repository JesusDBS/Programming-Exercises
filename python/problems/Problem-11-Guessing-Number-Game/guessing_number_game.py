# Guessing number game:
# Create a program in which the user guess a random integer number.

import sys
import random


class NumberError(Exception):
    """Check if n in the range of guessing
    """

    def __init__(self, n, message="n is out of range"):
        self.n = n
        self.message = message

        super().__init__(self.message)

    def __str__(self):
        return f"{self.n}! --> {self.message}"


def main(n_from, n_to, n_guessed):
    warning = f'{n_from} must be an integer'

    assert isinstance(n_from, int), warning
    assert isinstance(n_to, int), warning
    assert isinstance(n_guessed, int), warning

    if n_from > n_to:
        n_from, n_to = n_to, n_from

    n_correct = random.randint(n_from, n_to)

    if n_guessed == n_correct:
        print(f'Congratulations! Your guess {n_guessed} is correct!')
        return True

    print(
        f'Oh Sorry! Your guess {n_guessed} is not correct, please try again.')
    return False


if __name__ == '__main__':

    numbers = list(map(eval, sys.argv[1:]))
    n_from = numbers[0]
    n_to = numbers[1]
    n_guessed = numbers[2]

    if n_guessed < n_from or n_guessed > n_to:
        raise NumberError(n_guessed)

    check = main(n_from, n_to, n_guessed)
