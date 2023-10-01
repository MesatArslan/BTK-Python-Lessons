#1-Which of the 2 numbers entered is greater.
# a = input("1.number: ")
# b = input("2.number: ")

# result = (a > b)
# print(f'a:{a} b:{b} den büyüktür: {result}')

#2-Get 2 midterm (60%) and final (40%) grades from the user and calculate the average.
#3-If the everage is 50 and above, print it out if not not passed.

# a = float(input("1.midterm: "))
# b = float(input("2.midterm: "))
# c = float(input("Final: "))

# result = ((a + b)%60 + (c%40))

# print(f'Average: {result}  Course passing statues:{result >=50} ')


#4-Print the negative or positive case of the entered number.

# number = input("number: ")

# posneg = (int(number) >0)
# print(f'Statues of number: Positive   {posneg}')
#5-Print whether the entered number is odd or even.

# number = input("Number:")


# oddeven = (int(number) % 2 == 0)
# print(f'Statues of number: Even  -{oddeven}')

#6-Ask for the password and emaill information and check that is correct. ( email: sadikturan@email.com   password: abc123)

email = input("Email: ")
password = input("Password: ")

em = (email == 'sadikturan@email.com'.lower().strip() )
pas = (password == 'abc123')
print(f'Email is correct: {em} and Password is correct:{pas}')