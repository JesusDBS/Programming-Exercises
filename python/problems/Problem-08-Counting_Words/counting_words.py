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
import re

def count_words(string):
    """Counts the words contained in the string inserted by the user.

    Parameters
    ----------
    string: str
    """
    #validations
    assert any(string), "The string can't be an empty string!"

    #Cleaning string
    string = list(string.lower().split(' '))
    string = list(filter(lambda word: word, string))
    string = [re.sub("[^a-zA-Z]+", "",character) for character in string]

    words = dict.fromkeys(set(string), 0)

    #Counting words
    for key in words.keys():
        words[key] = len(list(filter(lambda word: word == key, string)))

    for key, val in words.items():
        print(f'The word "{key}" appears {val} times in your string!')

#----------------------------------------------------
def main():
    string = input("Insert your string: ")
    count_words(string)
#----------------------------------------------------
if __name__ == "__main__":
    main()