"""Function to use the database"""
import psycopg2
from config import identify


def get_results(query):
    """Set up database connection, execute query and close all"""
    user = identify()
    connect_str = "dbname='{}' user='{}' host='localhost' password='{}'".format(user[0], user[1], user[2])
    connection = False
    try:
        connection = psycopg2.connect(connect_str)
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
    except psycopg2.DatabaseError:
        raise DatabaseError
    else:
        return rows
    finally:
        if connection:
            connection.close()


def main():
    print("Error. Start 'main.py'")

if __name__ == '__main__':
    main()
