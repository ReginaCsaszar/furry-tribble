"Main program file, start program with this"

import data
import ui


def handle_menu():
    """Set the menu title and options"""
    title = "Application process menu"
    exit_option = "Exit"
    options = ["List the names of the mentors",
               "List the nick_name-s of all mentors working at Miskolc",
               "Find Carol's full name and phone number",
               "Find the girl who went to the Adipiscingenimmi University",
               "Add Markus Schaffarzyk into the application process",
               "Update Jemima Foreman's phone number",
               "Delete Arsenio and his friend",
               "Reset applicants table"]
    ui.print_menu(title, options, exit_option)


def choose():
    """Allow to choose an option, and start connected functions\n
    returns boolean: True for stay in the menu, False at exit
    """
    option = input("Please enter a number: ")
    if option == "1":
        data.mentors_names()
    elif option == "2":
        data.nicknames()
    elif option == "3":
        data.find_carol()
    elif option == "4":
        data.find_another_girl()
    elif option == "5":
        data.add_markus()
    elif option == "6":
        data.update_jemima()
    elif option == "7":
        data.delete_mauriseu_friends()
    elif option == "8":
        data.reset()
    elif option == "0":
        return False
    else:
        raise KeyError
    return True


def main():
    possible = True
    while possible:
        handle_menu()
        try:
            possible = choose()
        except KeyError:
            print("There is no such option.", end=" ")
            ui.back()


if __name__ == '__main__':
    main()
