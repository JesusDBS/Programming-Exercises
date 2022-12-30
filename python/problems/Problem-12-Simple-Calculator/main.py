# Simple Calculator
# Make a calculator software that can do various mathematical operations, use variables,
# and handle invalid user input in this project.

from app.user_interface import UserInterface


def main():
    flag = False
    while True:
        if not flag:
            print('To get out press space key in keyboard')
            user_input = input('Insert input: ')
        else:
            print(
                f'Do you want to continue with {UserInterface.buffer} or clear? For clear type "C", to continue type "N."\n')
            user_input = input('Insert input: ')
            if user_input.lower() == 'c':
                UserInterface.clen_buffer()
                continue

            if user_input.lower() == 'n':
                user_input = input(f'Insert input: {UserInterface.buffer}')
                user_input = f'{UserInterface.buffer} {user_input}'
                UserInterface.clen_buffer()

        if bool(user_input):
            UserInterface.get_input(user_input)
            values = UserInterface.validate_input()
            UserInterface.do_operation(values)
            print(f'The result is {UserInterface.buffer}')
            flag = True
        else:
            print('Good Bye!')
            break


if __name__ == "__main__":
    main()
