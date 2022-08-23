from random import randint
from connectors import my_connector
from termcolor import colored
import psycopg2


def generate_data():
    connection = my_connector.connect()

    # Reset orders table
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM orders")
        print(cursor.rowcount, "rows was deleted from table orders.")
        cursor.execute("ALTER SEQUENCE orders_id_seq RESTART")
        connection.commit()

    except psycopg2.Error as e:
        print(colored("Failed to update record to database.", e, "red"))
        connection.rollback()

    # Update orders table with 100 new orders
    try:
        cursor = connection.cursor()

        for i in range(100):
            # Generate only those ids' that are currently present in the user table
            user_id = randint(1, 10)
            order_time = randint(1, 10)

            # Execute query
            cursor.execute("INSERT INTO orders(USER_ID, TIME) VALUES ('%s', '%s')" % (user_id, order_time))
        connection.commit()

    except psycopg2.Error as e:
        print(colored("Failed to update record to database.", e, "red"))
        connection.rollback()

    finally:
        if not connection.closed:
            connection.close()
            print(colored("Table was succesfully updated. PostgreSQL connection was closed.", "green"))


generate_data()
