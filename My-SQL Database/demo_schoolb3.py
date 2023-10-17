import mysql.connector
from datetime import datetime
from connection import connection


#4- Write the following queries.
class Student:
        connection = connection
        mycursor = connection.cursor()
        
        @staticmethod
        def StudentInfo():
# a- Include all student records.

                # sql = "SELECT * FROM Student"
                # sql = "SELECT * FROM Student LIMIT 3"


# b -Obtain only student number, name and surname information of all students.

                # sql = "SELECT studentNumber, Name, Surname FROM Student"

# c- Take only the names and surnames of female students.

                # sql = "SELECT Name, Surname FROM Student WHERE Gender = 'F'"

# d- Get information about students born in 2003.

                # sql = "select * from Student Where YEAR(birthdate) = 2003"
                # sql = "select * from Student Where DAY(birthdate) = 6"
                # sql = "select * from Student Where MONTH(birthdate) = August"

# e- Get student information whose name is Ali and date of birth is 2005.
                # sql = "select name,birthdate from student where name = 'Ali' and YEAR(birthdate) = 2005"
# f- Take the records containing the expression 'an' in the name or surname.

                # sql = "Select name ,surname from student where name LIKE '%an%' or surname like'%an%'"
# g- How many male students are there?

                sql = "Select Count(*)from student where gender ='M'"

# h- Bring the female students in alphabetical order.
                
                sql = "Select name,surname from student where gender ='F' order by name, surname"


                Student.mycursor.execute(sql)

                try:
                        results = Student.mycursor.fetchall()
                        # print(results)
                        for result in results:
                        #     print(result[0])
                        #     print(f'name: {result[2]} surname: {result[2]}')
                        #     print(f'{result[1]}--{result[2]} {result[3]}')
                        #     print(f'name:{result[0]} birthyear: {result[1]}')
                            print(result)
                except mysql.connector.Error as err:
                        print('Error', err)
                finally:
                        Student.connection.close()

        
        # for student in result: # a
        #     print(student)

Student.StudentInfo()
