import cgi
import sqlite3

params = cgi.FieldStorage()

name = params.getfirst('name', '')
price = params.getfirst('price', '0')

print('Content-type: text/html\n')

connection = sqlite3.connect('data.db')
#connection = sqlite3.connect('cgi-bin/data.db')

cursor = connection.cursor()

cursor.execute('insert into goods(name, price) values("{}", {})'.format(name, price))

connection.commit()

connection.close()