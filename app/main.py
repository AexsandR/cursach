import mysql.connector
import os
from dotenv import load_dotenv
from generation.generation_name import Generation_people
load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD
)
print(conn.is_connected())

generation_people = Generation_people(conn)
generation_people.generation_clients(20)

conn.close()

