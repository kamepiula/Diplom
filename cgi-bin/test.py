import sqlite3
import json

print('Content-type: text/html\n')

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

cursor.execute('select * from goods')
x = cursor.fetchall()

html = '<table border="1px" width="300px" align="center">'
for i in x:
    html += '<tr>'
    for j in i:
        html += '<td>' + str(j) + '</td>'
    html +='</tr>'
html += '</table>'

y = json.dumps(html)

print(y)



connection.close()