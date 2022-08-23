from connectors import my_connector
from termcolor import colored
import psycopg2
import names
import randominfo


def generate_data():
    connection = my_connector.connect()

    # Reset app_user table
    try:
        cursor = connection.cursor()
        # OPTIONAL: check for foreign keys violation
        # For generating data for all tables, simply delete all data from all tables
        cursor.execute("DELETE FROM orders")
        print(cursor.rowcount, "rows was deleted from orders.")

        # Delete from table app_user
        cursor.execute("DELETE FROM app_user")
        print(cursor.rowcount, "rows was deleted from app_user.")

        # Reset app_user_id sequence
        cursor.execute("ALTER SEQUENCE app_user_id_seq RESTART")
        connection.commit()

    except psycopg2.Error as e:
        print(colored("Failed to update record to database.", e, "red"))
        connection.rollback()

    # Update customer table with 10 new customers
    try:
        cursor = connection.cursor()

        for i in range(10):
            first_name = names.get_first_name()
            last_name = names.get_last_name()
            email = first_name.lower() + "@gmail.com"
            date_of_birth = randominfo.get_date()

            # Execute query
            cursor.execute(
                "INSERT INTO public.app_user(FIRST_NAME, LAST_NAME, EMAIL, DATE_OF_BIRTH) "
                "VALUES ('%s', '%s', '%s', '%s')" % (
                    first_name, last_name, email, date_of_birth))

        connection.commit()
        print("Table app_user has been updated.")

    except psycopg2.Error as e:
        print(colored("Failed to update record to database.", e, "red"))
        connection.rollback()

    finally:
        if not connection.closed:
            connection.close()
            print(colored("Table was successfully updated. PostgreSQL connection was closed.", "green"))


generate_data()
