import sqlite3
import json

print("Content-type: text/html")

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

cursor.execute('select * from goods')

x = cursor.fetchall()

y = json.dumps(x)

print(y)

connection.close()