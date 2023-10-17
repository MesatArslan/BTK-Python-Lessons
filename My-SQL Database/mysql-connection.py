import mysql.connector

# Connection database
mydb = mysql.connector.connect(
    host = 'localhost', #192.23.43.57
    user = 'root',
    password = 'Justmysql1234',
    database = 'mydatabase'
)
### New database creating

# mycursor = mydb.cursor()

# mycursor.execute('SHOW DATABASES')
# # mycursor.execute('CREATE DATABASE mydatabase')

# for x in mycursor:
#     print(x)

# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers(name VARCHAR(255),address VARCHAR(255))")

print(mydb)

