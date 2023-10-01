#1- Write the function that prints the sent word on the screen at the specified time.

# def writeit(word , piece):
#     print(word*piece)

# writeit('apple\n',10)

#2- Write a function that converts an unlimited number of parameters sent to it to a list.

# def returnlist(*params):
#     liste=[]

#     for param in params:
#         liste.append(param)
    
#     return liste

# result = returnlist(10,20,30,70,'Hello')
# print(result)



#3- Find all prime numbers beetwen 2 sent numbers.

# def FindPrimenumbers(number1,number2):
#     for number in range(number1,number2+1):
#         if number > 1:
#             for i in range(2,number):
#                 if (number % i == 0):
#                     break
#             else :
#               print(number)

# number1 = int(input('Number1: '))
# number2 = int(input('Number2: '))

# FindPrimenumbers(number1,number2)

#4- Return all the divisors of a number sent to it as a list.

def Finddivisor(number):
    divisor = []
     
    for i in range(2,number):
      if (number % i == 0):
           divisor.append(i)
    
    return divisor

print(Finddivisor(40))
