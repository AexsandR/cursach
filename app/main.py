import mysql.connector

conn = mysql.connector.connect(
    host="100.117.159.15",
    user="bd",
    password="43400583_Ksu!"
)
print(conn.is_connected())