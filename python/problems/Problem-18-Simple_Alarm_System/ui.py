import os
import sys


class Option:
    """This class holds the logic to be executed when an user choose an option
    """
    def __init__(self, name_to_display: str, command, preparation_setp=None) -> None:
        self.name_to_display = name_to_display
        self.command = command
        self.preparation_step = preparation_setp

    def __call__(self):
        data = self.preparation_step() if self.preparation_step else None

        message = None
        if data or isinstance(data, int):
            message = self.command.execute(data)

        else:
            self.command.execute()

        if message:
            print(message)

    def __str__(self) -> str:
        return self.name_to_display
    
def get_user_input(label: str, required: bool = True) -> str:
    """Gets the user input
    """
    value = input(f'{label}: ') or None

    while required and not value:
        value = input(f'{label}: ') or None

    if value:
        value = int(value)

    return value
    
def get_new_alarm_data():
    """Gets the data for the new alarm
    """
    data = {
        "horas": get_user_input('Hora'),
        "minutos": get_user_input('Minutos', False),
        'segundos': get_user_input('Segundos', False)
        }
    
    data = {key : val for key, val in data.items() if val}
    return data

def get_edit_alarm_data():
    """Gets the data for editing an alarm
    """
    data = {
        "id": get_user_input("Identificador de la Alarma"),
        "horas": get_user_input('Hora'),
        "minutos": get_user_input('Minutos', False),
        'segundos': get_user_input('Segundos', False)
        }
    
    data = {key : val for key, val in data.items() if val or key == 'id'}
    return data

def get_delete_alarm_data():
    
    id =  get_user_input("Identificador de la Alarma")
    
    return int(id)

def print_options(options: dict) -> None:
    """Prints out the options to the user
    """
    for shorcut, option in options.items():
        print(f'({shorcut})', option)
    print()

def get_option_choice(options: dict) -> None:
    """Gets the option from user
    """
    while True:
        choice = input('Please select an option: ').upper()

        if choice not in options.keys():
            print('Invalid choice!')
            print_options(options)
        
        else:
            break
    
    if choice == 'Q':
        quit_program()
        
    choice = options.get(choice)

    clear_screen()
    choice()

def clear_screen() -> None:
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)

def quit_program() -> None:
    sys.exit()

def get_next_options() -> str:
    available_options = ('R', 'Q')
    next_option = input('Press R to return to menu or Q to exit: ').upper()

    while next_option not in available_options:
        clear_screen()
        next_option = input('Press R to return to menu or Q to exit: ').upper()

    return next_option
    