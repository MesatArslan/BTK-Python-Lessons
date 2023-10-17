
# 1- Create a database named schooldb with Workbench IDE and add the Student table.
# Id, StudentNumber, Name, Surname, Birthdate, Gender

# 2- Create the database connection.

#3- Create insert queries for the following information and add them to the records.
# ("101", "Ahmet", "Yilmaz", datetime. datetime (2005, 5, 17), "M")
# ("102", "Ali", "Can", datetime.datetime (2005, 6, 17), "M"),
# ("103", "Canan", "Tan", datetime. datetime(2005, 7, 7), "F"),
# ("104", "Ayse", "Taner", datetime.datetime (2005, 9, 23), "F"),
# ("105", "Bahadir", "Toksöz", datetime. datetime (2004, 7, 27), "M"),
# ("106", "Ali", "Cenk", datetime. datetime (2003, 8, 25), "M")

import mysql.connector
from datetime import datetime
from connection import connection # connection dosyasından connection ları aldık

class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self,studentNumber, name, surname, birthdate, gender):
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
    
    def saveStudent(self):
        sql = " INSERT INTO student(studentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
        value = (self.studentNumber, self.name,self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql,value)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} students added.')
        except mysql.connector.Error as err:
            print('Error', err)
        finally:
            Student.connection.close()
    
# ahmet = Student("202", "ahmet", " yilmaz", datetime(2005,5,17), "M")
# ahmet.saveStudent()   ## bir kişi ekleme
    @staticmethod
    def saveStudents(students):
        sql = " INSERT INTO student(studentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
        values = students
        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} students added.')
        except mysql.connector.Error as err:
            print('Error', err)
        finally:
            Student.connection.close()

students = [
("301", "Ahmet", "Yilmaz", datetime (2005, 5, 17), "M"),
("302", "Ali", "Can", datetime (2005, 6, 17), "M"),
("303", "Canan", "Tan",datetime(2005, 7, 7), "F"),
("304", "Ayse", "Taner", datetime (2005, 9, 23), "F"),
("305", "Bahadir", "Toksöz", datetime (2004, 7, 27), "M"),
("306", "Ali", "Cenk",  datetime (2003, 8, 25), "M")
]

Student.saveStudents(students)


####Second Way

# def insertStudent(studentNumber,Name,Surname,Birthdate,Gender):
#     connection = mysql.connector.connect(
#         host = 'localhost', #192.23.43.57
#         user = 'root',
#         password = 'Justmysql1234',
#         database = 'schooldb'
#     )

#     cursor = connection.cursor()

#     sql = "INSERT INTO schooldb(studentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s)"
#     values = (studentNumber,Name,Surname,Birthdate,Gender)

#     cursor.execute(sql,values)

#     try:
#      connection.commit()
#      print(f'{cursor.rowcount} student added.')
#      print(f'Id {cursor.lastrowid} of the last record.')
#     except mysql.connector.Error as err:
#      print('Error', err)
#     finally:
#      connection.close()
#      print('Data connection closed.')


# def insertStudent(list):
#     connection = mysql.connector.connect(
#         host = 'localhost', #192.23.43.57
#         user = 'root',
#         password = 'Justmysql1234',
#         database = 'schooldb'
#     )

#     cursor = connection.cursor()

#     sql = "INSERT INTO student(studentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
#     values = list

#     cursor.executemany(sql,values)

#     try:
#         connection.commit()
#         print(f'{cursor.rowcount} students added.')
#         print(f'Id {cursor.lastrowid} of the last record.')
#     except mysql.connector.Error as err:
#         print('Error', err)
#     finally:
#         connection.close()
#         print('Data connection closed.')


# list = []
# while True:
#    studentNumber = input("Student Number: ")
#    Name  = input("Student Name: ")
#    Surname  = input("Student Surname: ")
#    Birthdate= input("Student Birthdate(2000,09,25): ")
#    Gender = input("Student Gender(M/F): ")

#    list.append((studentNumber,Name,Surname,Birthdate,Gender))
#    result = input("Do you want to countinue?(e/h)")
#    if result == 'h':
#       print('Your records are transferred to database...')
#       print(list)
#       insertStudent(list)
#       break



### Third Way
# mycursor = connection.cursor()

# sql = " INSERT INTO student(studentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"

# students = [
# ("101", "Ahmet", "Yilmaz", datetime (2005, 5, 17), "M"),
# ("102", "Ali", "Can", datetime (2005, 6, 17), "M"),
# ("103", "Canan", "Tan",datetime(2005, 7, 7), "F"),
# ("104", "Ayse", "Taner", datetime (2005, 9, 23), "F"),
# ("105", "Bahadir", "Toksöz", datetime (2004, 7, 27), "M"),
# ("106", "Ali", "Cenk",  datetime (2003, 8, 25), "M")
# ]

# mycursor.executemany(sql,students)

# try:
#     connection.commit()
#     print(f'{mycursor.rowcount} students added.')
# except mysql.connector.Error as err:
#     print('Error', err)
# finally:
#     connection.close()