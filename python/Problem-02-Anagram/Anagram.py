#Anagram:
#Write a function that receives two words (String) and returns true or false (Bool) 
# depending on whether they are anagrams or not.
    # - An Anagram consists of forming a word by rearranging ALL the letters of another initial word.
    # - It is NOT necessary to check that both words exist.
    # - Two words exactly alike are not anagrams.

#Exceptions
class WordError(Exception):
    """Check if a string of characters contain only letters.
    """
    def __init__(self, word, message="only can have letters"):

        #validations
        assert isinstance(word, str), 'word must be a string'

        self.word = word
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.word} -> {self.message}"

#main program
def main():
    word_1 = input("word 1: ")
    word_2 = input("word 2: ")

    anagram(word_1, word_2)


def anagram(word_1, word_2):
    """Check if word_1 and word_2 are anagrams or not.

    Parameters
    ----------
    word_1: str
    word_2: str
    """
    #validations
    assert isinstance(word_1, str), 'word_1 must be a string'
    assert isinstance(word_2, str), 'word_2 must be a string'

    word_1 = word_1.lower().strip()
    word_2 = word_2.lower().strip()

    if not word_1.isalpha():
        raise WordError(word_1)

    if not word_2.isalpha():
        raise WordError(word_2)

    if word_1 == word_2:
        print(f"{word_1} and {word_2} are the same word. They'r not anagrams!")

        return False

    if sorted(word_1) == sorted(word_2):
        print(f"{word_1} and {word_2} are anagrams!")

        return True

    else:
        print(f"{word_1} and {word_2} are not anagrams!")

        return False


if __name__ == "__main__":
    main()