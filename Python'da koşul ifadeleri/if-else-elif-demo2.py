'''
1-Check if a number entered is between 0-100.

x = float(input('Number: '))
result = (x > 0)  and ( x<100)

print(f'Number is between 0-100:{result}')

'''
# x = float(input('Number: '))
# result = (x > 0)  and ( x<100)
# if (x > 0)  and ( x<100):
#  print('Number is between 0-100.')
# else:
#  print('Number is not between 0-100:')



'''
2-Check if a number entered is a positive even number.
x = float(input('Number: '))
result = (x > 0)  and (x % 2 == 0)

print(f'Is entered number positive even: {result}')
'''
# x = float(input('Number: '))

# if (x > 0)  and (x % 2 == 0): 
#  print('Entered number is positive even.')
# else:
#  print('Entered number is not positive even.')
 


      
'''
3-Check in with your email and password information.
email = 'sadikturan@gmail.com'
password = 'abc123'

enteredemail = input('Email: ')
enteredpassword = input('Password: ')

result = (email == enteredemail) and (password == enteredpassword)

print(f'Is logging into the app succesfull : {result}')
'''

# email = 'sadikturan@gmail.com'
# password = 'abc123'

# enteredemail = input('Email: ')
# enteredpassword = input('Password: ')

# if (email == enteredemail): 
#    if (password == enteredpassword):
#      print('Logging into the app succesfull.')
#    else :
#      print('Wrong password.')
# else:
#  print('TRY AGAIN...')






'''
4-Compare the 3 entered nuumbers in terms of magnitude.
a = int(input('Number1: '))
b = int(input('Number2: '))
c = int(input('Number3: '))

result = (a > b) and (a > c)
print(f'a is the biggest number: {result}')

result = (b > a) and (b > c)
print(f'b is the biggest number: {result}')

result = (c > a) and (c > b)
print(f'c is the biggest number: {result}')
'''

# a = int(input('Numbera: '))
# b = int(input('Numberb: '))
# c = int(input('Numberc: '))

# if (a > b) and (a > c):
#  print('a is the biggest number.')

# elif (b > a) and (b > c):
#  print('b is the biggest number.')

# elif (c > a) and (c > b):
#  print('c is the biggest number.')




'''5-Get 2 midterm (60%) and 1 final (40%) grades from the user and calculate the average.
 If the average is 50 and above, write passed, otherwise fail.
 Even if the average is 50, the final grade must be at least 50.
 If you get 70 from the final, the average is doesn't matter.

midterm1 = float(input('Midterm1: '))
midterm2 = float(input('Midterm2: '))
Final =  float(input('Final: '))

average = ((midterm1 + midterm2)/2)*0.6 + (Final)*0.4

result= (average >= 50) and (Final >= 50) or (Final >= 70)

print(f'Final exam passed: {result} and student average is: {average}') 
'''

# midterm1 = float(input('Midterm1: '))
# midterm2 = float(input('Midterm2: '))
# Final =  float(input('Final: '))

# average = ((midterm1 + midterm2)/2)*0.6 + (Final)*0.4

# if (average >= 50) and (Final >= 50) or (Final >= 70):
#  print(f'Student passed and student average is: {average}')
# else:
#  print(f'Student fail and student average is: {average}')
 





'''6-Calculate the person's weight index by taking person's weight, height and name information.
 Formul: (weight/square of boy height)
 According to the table below, which group does the person belong to?
 0-18.4 => weak
 18.5-24.9 =>normal
 24.5-29.9 =>overweight
 30.0-39.9 =>fat(obese)
name = input('Name: ')
weight = float(input('Weight: '))
height = float(input('Height: '))

index = weight/(height**2)

weak = (index > 0) and ( index <= 18.4)
normal = (index >= 18.5) and ( index <= 24.9)
overweight = (index > 25) and ( index <= 29.9)
obese = (index > 30) and ( index <= 40)

print(f' Your weight index:{index} and Is {name} weak   : {weak}')
print(f' Your weight index:{index} and Is {name} weak   : {normal}')
print(f' Your weight index:{index} and Is {name} weak   : {overweight}')
print(f' Your weight index:{index} and Is {name} weak   : {obese}')
'''

name = input('Name: ')
weight = float(input('Weight: '))
height = float(input('Height: '))
index = weight/(height**2)


if (index > 0) and ( index <= 18.4):
 print(f'{name} weight index:{index} and you are weak.')
elif (index >= 18.5) and ( index <= 24.9):
 print(f'{name} weight index:{index} and you are normal.')
elif (index > 25) and ( index <= 29.9):
 print(f'{name} weight index:{index} and you are overweight.')
elif (index > 30) and ( index <= 40):
 print(f'{name} weight index:{index} and you are weak')
