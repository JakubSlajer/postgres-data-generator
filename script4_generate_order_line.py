from connectors import my_connector
from termcolor import colored
import psycopg2
from random import randint


def generate_data():
    connection = my_connector.connect()

    # Reset order_line table
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM order_line")
        print(cursor.rowcount, "rows was deleted from order_line table")
        cursor.execute("ALTER SEQUENCE order_line_id_seq RESTART")
        connection.commit()

    except psycopg2.Error as e:
        print(colored("Failed to update record to database.", e, "red"))
        connection.rollback()

    # Update order_line table with 1000 new orders
    try:
        cursor = connection.cursor()

        for i in range(1000):
            # Generate only those ids that are currently present in the order table
            order_id = randint(1, 100)
            # Same for products
            product_id = randint(1, 117)

            # Execute query
            cursor.execute("insert into order_line(ORDER_ID, PRODUCT_ID) VALUES ('%s', '%s')" % (order_id, product_id))

        connection.commit()

    except psycopg2.Error as e:
        print(colored("Failed to update record to database.", e, "red"))
        connection.rollback()

    finally:
        if not connection.closed:
            connection.close()
            print(colored("Table was succesfully updated. PostgreSQL connection was closed.", "green"))


generate_data()
