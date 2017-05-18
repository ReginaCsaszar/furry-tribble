import psycopg2
from main import print_table


def back():
    """Step back to menu for enter"""
    back = input("Press enter to continue")
    return None


def run_select_query(query):
    try:
        connect_str = "dbname='jeannie' user='jeannie' host='localhost' password='57231024'"
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute("""{0}""".format(query))
        rows = cursor.fetchall()
        return rows
    except Exception as error_msg:
        print("Can't connect to database.", error_msg)
        return None


def run_other_query(query):
    try:
        connect_str = "dbname='jeannie' user='jeannie' host='localhost' password='57231024'"
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute("""{0}""".format(query))
    except Exception as error_msg:
        print("Can't connect to database.", error_msg)
        return None


def mentors_names():
    query = "SELECT first_name, last_name FROM mentors;"
    table = run_select_query(query)
    if table:
        title_list = ["First name", "Last name"]
        print_table(table, title_list)
    back()


def nicknames():
    query = "SELECT nick_name FROM mentors WHERE city='Miskolc';"
    table = run_select_query(query)
    if table:
        title_list = ["Nickname"]
        print_table(table, title_list)
    back()


def find_carol():
    query = "SELECT CONCAT (first_name,' ',last_name), phone_number FROM applicants WHERE first_name='Carol';"
    table = run_select_query(query)
    if table:
        title_list = ["Full name", "Phone number"]
        print_table(table, title_list)
    back()


def find_another_girl():
    query = "SELECT CONCAT (first_name,' ',last_name), phone_number FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu';"
    table = run_select_query(query)
    if table:
        title_list = ["Full name", "Phone number"]
        print_table(table, title_list)
    back()


def add_markus():
    query = "INSERT INTO applicants (first_name, last_name, phone_number, email, application_code) "
    values = "VALUES ('Markus','Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823);"
    run_other_query(query + values)
    query = "SELECT * FROM applicants WHERE application_code='54823';"
    table = run_select_query(query)
    title_list = ["ID", "First name", "Last name", "Phone number", "Email", "Application code"]
    print_table(table, title_list)
    back()


def update_jemima():
    query = "UPDATE applicants SET phone_number='003670/223-7459' WHERE "
    values = "first_name = 'Jemima' AND last_name = 'Foreman';"
    run_other_query(query + values)
    query = "SELECT first_name, last_name, phone_number FROM applicants WHERE "
    table = run_select_query(query + values)
    if table:
        title_list = ["First name", "Last name", "Phone number"]
        print_table(table, title_list)
    back()


def delete_mauriseu_friends():
    query = "SELECT * FROM applicants "
    values = "WHERE email LIKE '%@mauriseu.net';"
    table = run_select_query(query + values)
    if table:
        query = "DELETE FROM applicants "
        run_other_query(query + values)
        print("Applicants deleted")
    else:
        print("Applicants not found")
    back()


def reset():
    query = "SELECT * FROM applicants WHERE "
    values = "application_code='54823';"
    table = run_select_query(query + values)
    if table:
        modify_query = "DELETE FROM applicants WHERE "
        run_other_query(modify_query + values)
        print("Markus deleted.")
    values = "phone_number='003670/223-7459';"
    table = run_select_query(query + values)
    if table:
        modify_query = "UPDATE applicants SET phone_number='003620/834-6898' WHERE "
        run_other_query(modify_query + values)
        print("Jemina's phone number changed back to original.")
    values = "email LIKE '%@mauriseu.net';"
    table = run_select_query(query + values)
    if not table:
        query = "INSERT INTO applicants (first_name, last_name, phone_number, email, application_code) "
        values = "VALUES ('Arsenio', 'Matthews', '003620/804-1652', 'semper.pretium.neque@mauriseu.net', 39220);"
        run_other_query(query + values)
        values = "VALUES ('Ursa', 'William', '003620/496-7064', 'malesuada@mauriseu.net', 91220);"
        run_other_query(query + values)
        print("Arsenio and his friend added into the database.")
    print("\nEverything is at their original value.\n")
    back()


def main():
    print("Wrong file. Please run 'main.py' for Application process.")

if __name__ == '__main__':
    main()
