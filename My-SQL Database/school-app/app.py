from dbmanager import DbManager
import datetime
from Student import Student



class App:
    def __init__(self):
        self.db = DbManager()

    def initapp(self):
        msg = "*****\n1-Student list\n2-Add student\n3-Update student\n4-Delete student\n5-Add teacher\n6-Courses by class\n7-Exit(E/Ç)"

        while True:
            print(msg)
            process = input("Process: ")

            if process == '1':
                self.displayStudents()
                
            elif process == '2':
                self.addStudent()
            elif process == '3':
                self.editStudent()
            elif process == '4':
                pass
            elif process == '5':
                pass
            elif process == '6':
                pass
            elif process == '7':
                pass
            elif process == 'E' or process == 'Ç':
                break
            else:
                print('Wrong select...')
    
    def displayClasses(self):

        classes = self.db.getClasses()
        for c in classes :
            print(f'{c.id}: {c.name}')

    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Student id: "))

        student = self.db.getStudentById(studentid)
        student[0].name = input("Name:") or student[0].name
        student[0].surname = input("Surname:") or student[0].surname
        student[0].gender = input("Gender(F/M):") or student[0].gender
        student[0].classid = input("Class:") or student[0].classid
        
        year = input("Year") or student[0].birthdate.year
        month = input("Month") or student[0].birthdate.month
        day = input("Day") or student[0].birthdate.day
        student[0].birthdate = datetime.date(year,month,day)

        self.db.editStudent(student[0])

    def addStudent(self):
        self.displayClasses()
        classid = int(input("Which class: "))
        number = int(input("Student Number: "))
        name = input("Name: ")
        surname = input("Surname: ")
        year = int(input("Year: "))
        month = int(input("Month: "))
        day = int(input("Day: "))
        birthdate = datetime.date(year,month,day)
        gender = input("Gender (F/M): ")

        student = Student(None,number,name,surname,birthdate,gender,classid)
        self.db.addStudent(student)
    


    def displayStudents(self):
        self.displayClasses()
        classid = int(input("Which class: "))

        students = self.db.getStudentsByClassId(classid)
        print('Student list')
        for std in students:
            print(f'{std.id}-{std.name} {std.surname}')

        return classid


app = App()
app.initapp()
                
           