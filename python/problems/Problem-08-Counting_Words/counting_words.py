#!/usr/bin/env python3
"""
Author: Jesús David Briceño <jesusbingucv@gmail.com>
Purpose: Count words.
"""
#---------------------------------------------------
#Counting Words:
#Create a program that counts how many times each word is repeated and displays the final count of all of them
# - Punctuation marks are not part of the word.
# - A word is the same even if it appears in upper and lower case.
# - You cannot use language functions that solve it automatically.

#---------------------------------------------------
def count_words(string):
    """Counts the words contained in the string inserted by the user.

    Parameters
    ----------
    string: str
    """
    #validations
    assert any(string), "The string can't be an empty string!"
    pass

#----------------------------------------------------
def main():
    string = input("Insert your string: ")
    print(count_words(string))

#----------------------------------------------------
if __name__ == "__main__":
    main()