"""Function to use the database"""
import psycopg2
from config import identify


def get_results(query):
    user = identify()
    connect_str = "dbname='{}' user='{}' host='localhost' password='{}'".format(user[0], user[1], user[2])
    connection = psycopg2.connect(connect_str)
    cursor = connection.cursor()
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows


def main():
    print("Error. Start 'main.py'")

if __name__ == '__main__':
    main()
