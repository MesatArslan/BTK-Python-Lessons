# #Class

# class Person:
#     #class attributes
#     address = 'No information'
#     #constructor ( yapıcı method)
#     def __init__(self, name, year):

#          #object attributes
#          self.name = name
#          self.year = year
#          print('self method worked')
#     #instance methods
#     def intro(self):
#          print('Hello there. I am '+ self.name)

#     def calculateage(self):
#          return 2023 - self.year
         

# #Object (instance)
# p1 = Person(name= 'Mehmet', year= 1990)
# p2 = Person('Ali', 2001)


# p1.intro()
# p2.intro()

# print(f'My name: {p1.name}, My age: {p1.calculateage()}')
# print(f'My name: {p2.name}, My age: {p2.calculateage()}')


class Circle:
    #class object attributes
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius

    #methods
    def calculatearound(self):
        return 2*(self.pi+self.radius)
    
    def calculatearea(self):
        return self.pi*(self.radius**2)

c1 = Circle()   #radius = 1
c2 = Circle(5)

print(f'c1: area = {c1.calculatearea()}, around = {c1.calculatearound()}')
print(f'c1: area = {c2.calculatearea()}, around = {c2.calculatearound()}')