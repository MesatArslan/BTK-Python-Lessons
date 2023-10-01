# # x = 10 

# # if x > 5 :
# #     raise Exception('x can not take a value bigger than 5 ')

# def check_password(psw):
#     import re
#     if len(psw) < 8:
#         raise Exception("Password must contain at least 7 character.")    
#     elif not re.search("[a-z]",psw):
#         raise Exception("Parola must contain lowercase letter.")
#     elif not re.search("[A-Z]",psw):
#         raise Exception("Parola must contain upperrcase letter")
#     elif not re.search("[0-9]",psw):
#         raise Exception("Parola must contain number.")
#     elif not re.search("[_@?]",psw):
#         raise Exception("Parola must contain alpha numeric character.")
#     elif re.search('\s',psw):
#          raise Exception("Parola must not contain space")

#     else: 
#         print('Current password')
# password = input('password: ')

# try:
#     check_password(password)

# except Exception as ex:
#     print(ex)
# else:
#     print('Current password: else')

# finally:
#     print('Validation compeleted.')

#---------------#


class Person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception('Namespace contain to many characters.')
        else:
            self.name = name


p = Person('aneflwaegawjşegaw',1991)