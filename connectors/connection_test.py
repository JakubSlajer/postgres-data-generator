import my_connector
import psycopg2

try:
    connection = my_connector.connect()
    curs = connection.cursor()
    assert curs != None
    print("Connection OK")

except psycopg2.Error as Error:
    print("Error occured", Error)
finally:
    connection.close()
