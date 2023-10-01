#Class

class Person:
    #class attributes
    address = 'No information'
    #constructor ( yapıcı method)
    def __init__(self, name, year):

         #object attributes
         self.name = name
         self.year = year
         print('self method worked')
    #methods


#Object (instance)
p1 = Person(name= 'Mehmet', year= 1990)
p2 = Person('Ali', 2001)

#updating
p1.name = 'Ahmet'
p2.address  = 'Kastamonu'
#accessing object attributes
print(f'p1: name: {p1.name}, year: {p1.year}, address : {p1.address}')
print(f'p2: name: {p2.name}, year: {p2.year}, address : {p2.address}')
print(p1)
print(p2)


