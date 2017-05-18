"Main program file, start program with this"


def nothing():
    """Some message to handle menu without content"""
    useless = input("There's nothing, press enter to continue")
    return None


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
               "Print mentors table",
               "Print applicants table"]
    print_menu(title, options, exit_option)


def print_menu(title, options, exit_message):
    """Print the menu"""
    print("\n", title, "\n")
    for index, option in enumerate(options):
        print(" {0}. {1}".format(index+1, option))
    print(" 0.", exit_message)


def choose():
    """Allow to choose an option, and start connected functions\n
    returns boolean: True for stay in the menu, False at exit
    """
    option = input("Please enter a number: ")
    if option == "1":
        nothing()
    elif option == "2":
        nothing()
    elif option == "3":
        nothing()
    elif option == "4":
        nothing()
    elif option == "5":
        nothing()
    elif option == "6":
        nothing()
    elif option == "7":
        nothing()
    elif option == "8":
        nothing()
    elif option == "9":
        nothing()
    elif option == "0":
        return False
    else:
        raise KeyError("There is no such option.")
    return True


def print_table(table, title_list):
    """Print table and title formatted\n
    only accept strings in lists
    """
    # setting the maximum lengths of the two coloumns for formatting
    max_lenght = []
    for i in range(len(title_list)):
        max_table = max([len(ta_row[i]) for ta_row in table])
        if max_table > len(title_list[i]):
            max_lenght.append(max_table + 2)
        else:
            max_lenght.append(len(title_list[i]) + 2)
    # print top line
    print("/", end="")
    for le in max_lenght:
        print("-" * le, end="--")
    print("\b\\\n|", end="")
    # print titles
    for lng, title in zip(max_lenght, title_list):
            print("{0:^{width}}".format(title, width=lng), "|", end="")
    print("")
    # print table and padding
    for row in table:
        print("|", end="")
        for lng in max_lenght:
            print("-" * lng, end="-|")
        print("\n|", end="")
        for lng, field in zip(max_lenght, row):
            print("{0:^{width}}".format(field, width=lng), "|", end="")
        print("")
    # print last line
    print("\\", end="")
    for le in max_lenght:
        print("-" * le, end="--")
    print("\b/")


def main():
    possible = True
    while possible:
        handle_menu()
        try:
            possible = choose()
        except KeyError as err:
            print("Error: ", err)


if __name__ == '__main__':
    main()
