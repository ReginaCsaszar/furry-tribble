"""Printing and menu handling functions"""

import os


def back():
    """Step back to menu for enter"""
    back = input("Press enter to continue")
    return None


def print_menu(title, options, exit_message):
    """Print the menu"""
    os.system("clear")
    print("\n", title, "\n")
    for index, option in enumerate(options):
        print(" {0}. {1}".format(index+1, option))
    print(" 0.", exit_message, "\n")


def print_table(table, title_list):
    """Print table and title formatted\n
    only accept strings in lists
    """
    os.system("clear")
    # setting the maximum lengths of the two coloumns for formatting
    max_lenght = []
    for i in range(len(title_list)):
        max_table = max([len(str(ta_row[i])) for ta_row in table])
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
    print("Wrong file. Please run 'main.py' for Application process.")


if __name__ == '__main__':
    main()
