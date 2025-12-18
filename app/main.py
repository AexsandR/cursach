import mysql.connector

conn = mysql.connector.connect(
    host="",
    user="",
    password=""
)
print(conn.is_connected())