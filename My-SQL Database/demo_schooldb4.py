import mysql.connector
from datetime import datetime
from connection import connection

# 5- Complete the following update questions.
# a- Update the information of a student you have accepted according to their id.
# b- Update the information of a student you have accepted according to gender.

class Student:
    
    connection = connection
    mycursor = connection.cursor()

    def __init__(self, id, studentNumber, name, surname, birthdate, gender):
        if id is None:
            self.id=0
        else:
            self.id =id
        self.studentNumber = studentNumber
        self.name = name 
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    @staticmethod 
    def getStudentById(id):
        sql = "select * from student where id=%s"
        value = (id,)

        Student.mycursor.execute(sql, value)

        try:
            obj =  Student.mycursor.fetchone()
            return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        except mysql.connector.Error as err:
            print ('Error', err) 
        

    # def getStudentInfo(id):
    # def updateStudentInfo(self):
    @staticmethod
    def updateStudents(liste):
        
        # sql = "Update student set Gender = 'F'  where id = 16"
        # sql = "Update student set id = 5  where id = 12 "
        sql = "Update student set studentNumber= %s,name = %s, surname=%s, birthdate= %s, gender = %s where id = %s"
        # values = (self.studentNumber, self.name, self.surname self.birthdate, self.gender,self.id)
        values = []
        order = [1,2,3,4,5,0]

        for item in liste:
            item = [item[i] for i in order]
            values.append(item)

        

        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print (f'{Student.mycursor.rowcount} record updated.')
        except mysql.connector.Error as err:
            print ('Error', err)

        
    @staticmethod 
    def getStudentsGender(gender):
        sql = "select * from student where gender=%s"
        value = (gender,)

        Student.mycursor.execute(sql, value)
        try:
            return Student.mycursor.fetchall()
        except mysql.connector.Error as err:
            print ('Error', err) 

        

    # getStudentInfo(id)
# student = Student.getStudentById(8)

# student.name= 'Cinar'
# student.surname = 'Turan'   

# student.updateStudentInfo()

students = Student.getStudentsGender('M')
print(students)

liste = []
for std in students:
    std = list(std)
    std[2] = 'Mr ' + std[2]
    liste.append(std)


Student.updateStudents(liste)
