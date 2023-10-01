
# Methods


# list = [1,2,3]

# list.append(4)
# list.pop()

# print(type(list))
# print(list)

# myString = 'Hello'
# print(myString.upper())
# print(type(myString))


# Functions

# def sayHello(name = 'user'):
#     print('hello ' + name)

# sayHello('Çınar')
# sayHello('Ahmet')
# sayHello()


def sayHello(name = 'user'):
    return 'hello ' + name

msg = sayHello('Çınar')

print(msg)


def total(num1, num2):
    return num1 + num2

result = total(10,30)
result = total(50,30)

print(result)

def agecalculate(bornYear):
    return 2023 - bornYear

ageÇınar = agecalculate(2017)
ageAdem = agecalculate(2015)
ageBatu = agecalculate(2010)

print(ageÇınar,ageAdem,ageBatu)


def Howmanyyearsuntilretirement(bornyear,name):
    '''
    DOCSTRİNG: How many years are left until your retirement based on your birth year.
    INPUT: Birth year
    OUTPUT: Calculated year information
    '''
    age = agecalculate(bornyear)
    retirement = 65 - age

    if retirement > 0:
        print(f'{retirement} years until your retirement.')
    else:
        print(f'You are retirement.')


Howmanyyearsuntilretirement(1980, 'Ahmet')
Howmanyyearsuntilretirement(1990, 'Mehmet')
Howmanyyearsuntilretirement(1930, 'Yusuf')

print(help(Howmanyyearsuntilretirement))
