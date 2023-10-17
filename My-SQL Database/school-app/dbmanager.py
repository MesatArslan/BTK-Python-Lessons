import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class



class DbManager:
    def __init__(self):
        self.connection= connection
        self.cursor = self.connection.cursor()

    
    
    def getStudentById(self, id):
        sql = "SELECT * FROM student where id = %s"
        value = (id,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchone()
            if obj:
                return Student.CreateStudent(obj)
            else:
                return None
        except mysql.connector.Error as err:
            print('Error', err)
    
    def getClasses(self):
        sql = "SELECT *  FROM  Class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print('Error',err)
        ####
    # def getTeacherById(self, id):
    #     sql = "SELECT *  FROM  teacher where id = %s"
    #     value = (id,)
    #     self.cursor.execute(sql,value)
    #     try:
    #         obj = self.cursor.fetchone()
    #         return Teacher.CreateTeacher(obj)
    #     except mysql.connector.Error as err:
    #         print('Error',err)
        

    def getStudentsByClassId(self, classid):
        sql = "SELECT *  FROM  student where classid = %s"
        value = (classid,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Error',err)
        

    def addStudent(self,student: Student):
        sql = " INSERT INTO student(studentNumber,Name,Surname,Birthdate,Gender,Classid) VALUES(%s,%s,%s,%s,%s,%s)"
        value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender,student.classid)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} student added.')
        except mysql.connector.Error as err:
            print('Error', err)
        
       
    def editStudent(self,student: Student):
        sql = "Update student set name = %s, surname=%s, birthdate= %s, gender = %s, classid= %s where id = %s"
        value = (student.id ,student.name, student.surname, student.birthdate, student.gender, student.classid)
        self.cursor.execute(sql,value)
        student = Student( "12345", "John", "Doe", "2000-01-01", "Male",'2' )
        # There is a problem solve this
    

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} student updated.')
        except mysql.connector.Error as err:
            print('Error', err)
    
    ###
    # @staticmethod
    # def AddOrEditstudent(self,student: Student):
    #     if id == 1:
    #         sql = "INSERT INTO student(studentNumber,Name,Surname,Birthdate,Gender,Classid) VALUES(%s,%s,%s,%s,%s,%s)"
    #         value = (student.studentnumber, student.name, student.surname, student.birthdate, student.gender,student.classid)
    #         self.cursor.execute(sql,value)

    #         try:
    #             self.connection.commit()
    #             print(f'{self.cursor.rowcount} student added.')
    #         except mysql.connector.Error as err:
    #             print('Error', err)

    #     elif id !=0:
    #         sql = "Update student set name = %s, surname=%s, birthdate= %s, gender = %s, classid= %s where id = %s"
    #         value = ( student.name, student.surname, student.birthdate, student.gender, student.classid, student.id)
    #         self.cursor.execute(sql,value)

    #         try:
    #             self.connection.commit()
    #             print(f'{self.cursor.rowcount} student updated.')
    #         except mysql.connector.Error as err:
    #             print('Error', err)
    
    # ###
    # def addTeacher(self,teacher: Teacher):
    #     sql = " INSERT INTO teacher(branch,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
    #     value = (teacher.branch, teacher.name, teacher.surname, teacher.birthdate, teacher.gender)
    #     self.cursor.execute(sql,value)
        

    #     try:
    #         self.connection.commit()
    #         print(f'{self.cursor.rowcount} teacher added.')
    #     except mysql.connector.Error as err:
    #         print('Error', err)

    def editTeacher(self,teacher: Teacher):
        pass

    #finally blocklarını yapmak yerine
    
    def  __del__(self):
        self.connection.close()
        print("db deleted.")


db = DbManager()

student = db.getStudentById(8)
if student:
    for s in student:
      print(s.name)
    print(s.surname)
else:
    print("Student not found")


# students = db.getStudentsByClassId(1)
# print(students[0].name)
# print(students[4].name)

# student = db.getStudentById(8)
# db.addStudent(student[0])
# # std = student(None,102,...)
# student[0].name = "Mr Mehmet"
# student[0].surname = "Turan"
# student[0].studentnumber = "501"


# student = db.getStudentById()
# # student[0].name = "Mr Burak"
# student[0].name = "Mr Mustafa"
# db.editStudent(student[0])


# # student = db.getStudentById()
# # student[0].name = "Deniz"
# # student[0].surname = "Atilgan"
# # student[0].studentnumber= "505"
# # db.AddOrEditstudent(student)

# Teacher = db.getTeacherById(4)
# Teacher[0].name = "Murat"
# Teacher[0].surname = "Sanik"
# Teacher[0].branch = "History"

# db.addTeacher(Teacher)