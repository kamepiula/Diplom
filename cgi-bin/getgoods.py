import sqlite3
import json

print('Content-type: text/html\n')

connection = sqlite3.connect('data.db')
#connection = sqlite3.connect('cgi-bin/data.db')
cursor = connection.cursor()

cursor.execute('select * from goods')
x = cursor.fetchall()
#[[1,'велосипед',1600, None],[...],[...]]
#преобразуем в формат JSON


# html = '<table border="1px" width="300px" align="center">'
# for i in x:
#     html += '<tr>'
#     for j in i:
#         html += '<td>' + str(j) + '</td>'
#     html += '</tr>'
# html += '</table>'


y = json.dumps(x)

print(y)
connection.close()