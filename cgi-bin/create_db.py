import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

sql = '''create table if not exists goods(
id integer primary key autoincrement,
name text,
price integer, 
comment text
)
'''

cursor.execute(sql)

cursor.execute('insert into goods(name, price) values("Самолет", 1000)')
cursor.execute('insert into goods(name, price) values("Пароход", 2000)')
cursor.execute('insert into goods(name, price) values("Снегоход", 3)')

connection.commit()

cursor.execute('select * from goods')
x = cursor.fetchall()
print(x)

connection.close()