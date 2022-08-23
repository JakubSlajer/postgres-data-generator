from connectors import my_connector
from termcolor import colored
import psycopg2
import fruit_stand


def generate_data():
    connection = my_connector.connect()

    # Find any rows in the product table
    try:
        cursor = connection.cursor()

        cursor.execute("DELETE FROM products")
        print(cursor.rowcount, "rows was deleted")
        cursor.execute("ALTER SEQUENCE products_id_seq RESTART")
        connection.commit()

    except psycopg2.Error as e:
        print(colored("Failed to update record to database.", e, "red"))
        connection.rollback()

    try:
        cursor = connection.cursor()
        # Get list of all fruits
        fruits = fruit_stand.all_fruits()

        # For each fruit in fruit list, add fruit as row to the db
        for i in range(len(fruits)):
            fruit = fruits[i]

            if fruit == "Buddha's hand":
                fruit = "Buddha''s hand"

            cursor.execute("INSERT INTO products(NAME, IN_STOCK) VALUES ('%s', '%s')" % (fruit, 1))
        connection.commit()

    except psycopg2.Error as e:
        print(colored("Failed to update record to database.", e, "red"))
        connection.rollback()

    # At the end of generation don't forget to close the connection stream
    finally:
        if not connection.closed:
            connection.close()
            print(colored("Table was successfully updated. PostgreSQL connection was closed.", "green"))


generate_data()
