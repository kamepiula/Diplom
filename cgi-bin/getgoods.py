import sqlite3
import json

print('Content-type: text/html\n')

connection = sqlite3.connect('data.db')
#connection = sqlite3.connect('cgi-bin/data.db')
cursor = connection.cursor()

cursor.execute('select * from goods')
x = cursor.fetchall()

#преобразуем в формат JSON
y = json.dumps(x)

print(y)

connection.close()