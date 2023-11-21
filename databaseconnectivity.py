import mysql.connector as sq

con=sq.connect(host='localhost', user='root',
               password='1234', database='test')
cur=con.cursor()

cur.execute('select * from students;')

for x in cur:
    print(x)
