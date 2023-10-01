#1-Store the given students in the dictionary with the information you receive from the user.

#2-Get the student information from the users  and show relevant student information


students = {}


number = input("student no: ")
name = input ("student name:")
surname = input("student surname:")
phone = input("student phone:")

# students[number]={
#     'Name': name,
#     'surname': surname,
#     'Phone': phone
# }

students.update({
    number:{
       'name' : name,
       'surname': surname,
       'phone': phone
    }
})

number = input("student no: ")
name = input ("student name:")
surname = input("student surname:")
phone = input("student phone:")

students.update({
    number:{
       'name' : name,
       'surname': surname,
       'phone': phone
    }
})

number = input("student no: ")
name = input ("student name:")
surname = input("student surname:")
phone = input("student phone:")

students.update({
    number:{
       'name' : name,
       'surname': surname,
       'phone': phone
    }
})

print(students)

print('*'*50)

stdno = input('student no:')
student = students[number]

print(f"Aradiginiz {stdno} nolu öğrencinin adi:{student['name']} soyadi:{student['surname']} ve telefonu: {student['phone']}")

print(student)