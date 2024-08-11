
from reloj import reloj_commands as commands
from ui import Option, clear_screen, get_new_alarm_data, get_edit_alarm_data, \
    get_delete_alarm_data, print_options, get_option_choice, get_next_options, quit_program


def main():
    """Main loop of the program
    """
    clear_screen()
    options = {
        'A': Option('Add a new alarm', commands.CreateNewAlarmCommand(), get_new_alarm_data),
        'B': Option('Edit an alarm', commands.EditAlarmCommand(), get_edit_alarm_data),
        'C': Option('Delete an alarmn', commands.DeleteAlarmCommand(), get_delete_alarm_data),
        'D': Option('Get current time', commands.GetCurrentTimeCommand()),
        'E': Option('Display active alarms', commands.DisplayAlarmsCommand()),
        'Q': 'Exit'
    }

    print_options(options)
    get_option_choice(options)
    print()

    next_option = get_next_options()

    if next_option == 'R':
        main()

    if next_option == 'Q':
        quit_program()

  
if __name__ == '__main__':
   main()