import cgi
import sqlite3

params = cgi.FieldStorage()

ids = params.getfirst('id', '')


print('Content-type: text/html\n')

connection = sqlite3.connect('data.db')

cursor = connection.cursor()
cursor.execute('delete from goods where id={}'.format(ids))

connection.commit()

connection.close()