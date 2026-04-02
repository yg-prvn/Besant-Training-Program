# Database Config

import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    port = "3306",
    user = "root",
    password = "ninanina",
    database = "world"
)

# Cursor - Executes MySQL Queries

cur = conn.cursor()

cur.execute("SELECT * FROM CITY")

result = cur.fetchall()

for row in result:
    print(row)

cur.close()
conn.close()