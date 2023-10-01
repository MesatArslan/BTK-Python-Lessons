# error handling => hata yönetimi
# try:
#     x = int(input('x : '))
#     y = int(input('y : '))
#     print(x/y)

# # except ZeroDivisionError:
# #     print('0 can not be entered for y')

# # except ValueError:
# #     print('You must enter a numeric value for x and y')

# except (ZeroDivisionError, ValueError) as e:
#     print('You entered a wrong number')
#     print(e)

#--------------------#
# try:
#     x = int(input('x : '))
#     y = int(input('y : '))
#     print(x/y)


# except:
#     print('You entered a wrong number')


#--------------------#
while True:
    try:
        x = int(input('x : '))
        y = int(input('y : '))
        print(x/y)


    except Exception as ex :
        print('You entered a wrong number', ex)
    else:
        break
    finally:
        print('try except is finished.')
