import psycopg2


def connect():
    db = psycopg2.connect(
        user="postgres",
        password="postgres",
        database="postgres",
        host="localhost",
        port="5433"
    )

    return db
