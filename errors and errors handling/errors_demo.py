liste = ['1', '2', '5a', '10b','abc', '10', '50']

#1- Find the numeric values in the list element.

# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue

#2- Make sure every input you get is a number unless the user enters a 'q' value otherwise write an error message.

# while True:
#     number = input('number: ')
#     if number == 'q':
#         break

#     try:
#         result = float(number)
#         print('Entered number :', result)
#         break
#     except ValueError:
#         print('Invalid number.')
#     continue

#3- Write turkish character error in the entered password error.

# def checkPassword(password):

#     turkish_characters = 'şçüöğıİ'


#     for i in password:
#         if i in turkish_characters:
#             raise TypeError('Password does not contain turkish carachters.')
#         else:
#             pass

#     print('Valid password.')

# password = input('password: ')

# try:
#     checkPassword(password)
# except TypeError as err:
#     print(err)


#4- Create the factorial function and give error messages for the value that comes to the function.

def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError('Negative value.')
    
    result = 1

    for i in range(1, x+1):
        result *= i

    return result

for x in [5, 10 ,20 ,-3, '10a']:
    try:
        y = faktoriyel(x)
    
    except ValueError as err:
        print(err)
        continue
    print(y)
