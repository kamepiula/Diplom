import cgi
import sqlite3

params = cgi.FieldStorage()

ids = params.getfirst('id', '')
name = params.getfirst('name', '')
price = params.getfirst('price', '0')

print('Content-type: text/html\n')

connection = sqlite3.connect('data.db')

cursor = connection.cursor()
cursor.execute('UPDATE goods SET name={} price={} WHERE id={}'.format(name, price, ids))

connection.commit()

connection.close()