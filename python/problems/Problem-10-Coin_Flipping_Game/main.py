#!/usr/bin/env python3
"""
Author: Jesús David Briceño <jesusbingucv@gmail.com>
Purpose: A program to play coin flipping.
"""
# ---------------------------------------------------
# Coin Flipping:
# Create a coin flipping game.

# ---------------------------------------------------

from coin import Coin
from player import Player


class ChoiceException(Exception):
    def __init__(self, choice, message='You must choose between Heads or Tails'):
        self.choice = choice
        self.message = message

        super().__init__(self.message)

    def __str__(self) -> str:
        return f"Your input is wrong: {self.choice}! --> {self.message}"


def clean_choice(choice: str):
    return choice.strip().lower()


def main():
    CHOISES = ['heads', 'tails']

    name = input("What's your name?: ")
    player = Player(name)
    coin = Coin()

    choice = input(f"Welcome {player.name}! Heads or Tails?: ")
    choice = clean_choice(choice)

    if choice not in CHOISES:
        raise ChoiceException(choice)

    player.choice = clean_choice(choice)
    is_heads = coin.tossing_coin()

    if is_heads and player.choice == 'heads':
        return f"Congratulations {player.name}! You got Heads!"

    if is_heads and player.choice == 'tails':
        return f"Oh Sorry {player.name}! You got Heads, try again!"

    if not is_heads and player.choice == 'heads':
        return f"Oh Sorry {player.name}! You got Tails, try again!"

    if not is_heads and player.choice == 'tails':
        return f"Congratulations {player.name}! You got Tails!"


if __name__ == "__main__":
    print(main())
