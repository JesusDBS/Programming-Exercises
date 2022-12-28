#!/usr/bin/env python3
"""
Author: Jesús David Briceño <jesusbingucv@gmail.com>
Purpose: Determine the maximum even number from a list of integers.
"""
# ---------------------------------------------------
# Maximum Even:
# Create a program that takes a list of integers and determine what is the maximum even number in such list.

# ---------------------------------------------------


def max_even(*args):
    """Determine the maximum even number from a list of integers.

    Parameters
    ----------
    *args: list
            List of integers.
    """
    even_list = []
    for n in args:
        assert isinstance(n, int), f'n: "{n}" must be an integer!'
        if n % 2 == 0:
            even_list.append(n)

    return max(even_list)


if __name__ == "__main__":
    print(max_even(1, 2, 3, 4, 6, 8, 10, 20, 25, 99,))
