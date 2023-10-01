#inheritance (Kalıtım): Miras alma

#Person => name, surname, age, eat(), run(), drink()

#Student(Person), Teacher(Person)

#Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print('Person created.')

    def who_am_i(self):
        print('I am a person.')

    def eat(self):
        print('I am eating.')

class Student(Person):
    def __init__(self, fname, lname, number):
        self.studentnumber = number
        Person.__init__(self, fname, lname)

        print('Student created.')
    
    #override
    def who_am_i(self):
        print('I am a student.')


class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname,lname)
        self.branch = branch
    

    def who_am_i(self):
        print(f'I am a {self.branch} teacher.')
    

p1 = Person('Ali', 'Yılmaz')
s1 = Student('Çınar', 'Turan', 12567)
t1 = Teacher('Erva', 'Aslan', 'Mathematic')

print(f'Person first name:{p1.firstname}, lastname: {p1.lastname}')
print(f'Student first name:{s1.firstname}, lastname: {s1.lastname} and my number is {s1.studentnumber}')

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()
p1.eat()
s1.eat()




