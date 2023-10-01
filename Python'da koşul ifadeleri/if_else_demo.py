#1-Check the user's licence status by, requesting name, age and education information. The condition for obtanin a licence must be at least 18 and the education level must be hisgh scholl or university.

# name = input('Name: ')
# age = int(input('Age: '))
# education = input('Education: ')

# if (age >= 18):
#     if (education == 'high school' or education =='university'):
#        print("You eligible for a driver's licence.")
#     else:
#        print("You are not eligible for a driver's licence because your education is under High School.")
        
# else :
#     print("You are not eligible for a driver's licence because your age is under 18.")
    


#2-Take 2 written and 1 oral grades of a student and print the grade information corresponding to the grade range according to the calculated average.
# 0-25  => 0
# 25-45 => 1
# 45-55 => 2
# 55-70 => 3
# 70-85 => 4
# 85-100=> 5

# a = int(input('Written1: '))
# b = int(input('Written2: '))
# c = int(input('Oral grades: '))

# result = ( a + b + c)/3

# if (0 <= result < 25):
#    print(f'Your average = {result} and your grade note = 0.')
# elif (25 <= result < 45): 
#    print(f'Your average = {result} and your grade note = 1.')
# elif (45 <= result < 55): 
#    print(f'Your average = {result} and your grade note = 2.')
# elif (55 <= result < 70): 
#    print(f'Your average = {result} and your grade note = 3.')
# elif (70 <= result < 85): 
#    print(f'Your average = {result} and your grade note = 4.')
# elif (85 <= result <= 100): 
#    print(f'Your average = {result} and your grade note = 5.')




#3-Calculate the service time of a vehicle with a registration date according to the following information.
# 1. Maintenance => 1.year
# 2. Maintenance => 2.year
# 3. Maintenance => 3.year
# **Calculate the duration based on the day, month, years information recevied.
# ***You need to use the datetime module.

# days = int(input('How many days car in traffic?: '))

# if 0 < days <= 365:
#     print('Car needs first year maintenance.')
# elif 365 < days <=730:
#     print('Car needs second year maintenance.')
# elif 730 < days <=1095:
#     print('Car needs third year maintenance.')
# else:
#  print('Hatalı süre bilgisi!!!')

import datetime

date = input('What date was your vehicle on the road(2019/9/6): ')
date = date.split('/')

# print(date[0])
# print(date[1])
# print(date[2])

release = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
now = datetime.datetime.now()
gap = now - release
gap1 = gap.days

if 0 < gap1 <= 365:
    print('Car needs first year maintenance.')
elif 365 < gap1 <=730:
    print('Car needs second year maintenance.')
elif 730 < gap1 <=1095:
    print('Car needs third year maintenance.')
else:
 print('Hatalı süre bilgisi!!!')




