#Inverting Strings:
#Create a program that reverses the order of a text string without using language functions that do it automatically.
# - If we pass "Hello world" it would return "odnum aloH".

def inverse_string(string):
    """Inverse a string inserted by the user.

    Parameters
    ----------
    string: str
    """
    #validations
    assert any(string), "The string can't be an empty string!"

    string = list(string.split(' '))

    #Eliminate blank spaces
    string = list(filter(lambda character: character, string))

    string_reverse_list = []
    string.reverse()

    for word in string:
        if word:
            word = list(word.strip())
            word.reverse()
            word = ''.join([letter for letter in word])
            string_reverse_list.append(word)

    if len(string_reverse_list) > 1:
        string_reverse_list = ' '.join([word for word in string_reverse_list])

        return string_reverse_list

    return string_reverse_list[0]


def main():
    string = input("Insert your string: ")
    print(inverse_string(string))


if __name__ == "__main__":
    main()