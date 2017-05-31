"""Module which generate content for templates"""


def prepare_content(filename):
    """Read and process file content\n
    return list of lists of strings
    """
    with open("./static/" + filename, "r") as file:
        lines = file.readlines()
    table = []
    for index in range(0, len(lines), 4):
        row = [lines[index].replace("\n", ""),
               lines[index+1].replace("\n", ""),
               lines[index+2].replace("\n", ""),
               lines[index+3].replace("\n", "")
               ]
        table.append(row)
    return table


def main():
    print("Error. Start 'main.py'")


if __name__ == '__main__':
    main()
