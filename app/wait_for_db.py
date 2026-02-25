import time
import psycopg
from decouple import config

while True:
    try:
        psycopg.connect(
            dbname=config("DB_NAME"),
            user=config("DB_USER"),
            password=config("DB_PASSWORD"),
            host=config("DB_HOST"),
            port=config("DB_PORT"),
        )
        break
    except psycopg.OperationalError:
        print("Waiting for PostgreSQL...")
        time.sleep(2)
