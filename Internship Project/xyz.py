import mysql.connector
 
# Connect to the MySQL server
con = mysql.connector.connect(host="localhost",user="root@localhost", password="sairaj", database="b1")
cursor = con.cursor()
 
cursor.execute("CREATE TABLE IF NOT EXISTS student (name VARCHAR(10), age INT, address VARCHAR(20));")
name = input("Enter name: ")
age = int(input("Enter age: "))
address = input("Enter address: ")

# Insert data into the "student" table
query = "INSERT INTO student VALUES ('{name}', {age}, '{address}');"
cursor.execute(query)
con.commit()
print("Data inserted successfully.")
cursor.close()
con.close()





img = PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=30,y=30)
