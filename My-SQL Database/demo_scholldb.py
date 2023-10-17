
# 1- Create a database named schooldb with Workbench IDE and add the Student table.
# Id, StudentNumber, Name, Surname, Birthdate, Gender

# 2- Create the database connection.

import mysql.connector


mydb = mysql.connector.connect(
    host = 'localhost', #192.23.43.57
    user = 'root',
    password = 'Justmysql1234',
    database = 'schooldb'
)

mycursor = mydb.cursor()

# # mycursor.execute("SHOW DATABASES")
# mycursor.execute('CREATE DATABASE schooldb')

# for x in mycursor:
#     print(x)

# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE Student(Id INT,StudentNumber VARCHAR(5),Name VARCHAR(45), Surname VARCHAR(50), Birtdate DATETIME, Gender CHAR(1))")

# print(mydb)