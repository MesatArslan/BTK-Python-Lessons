from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time

# import datetime

rightnow = datetime.now()
rightnow = datetime.today()


result= datetime.now()
result = rightnow.year
result = rightnow.month
result = rightnow.day
result = rightnow.hour
result = rightnow.minute
result = rightnow.second
result= datetime.ctime(rightnow)
result = datetime.strftime(rightnow,'%Y')
result = datetime.strftime(rightnow,'%X')
result = datetime.strftime(rightnow,'%A')
result = datetime.strftime(rightnow,'%d')
result = datetime.strftime(rightnow,'%B')
result = datetime.strftime(rightnow,'%Y %B %A')



# t = '21 April 2019'

# day, month, year = t.split()
# print(day)
# print(month)
# print(year)


t = '15 April 2023 hour 10:12:30'
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
result = result.year

birthday = datetime(1974,10,10,12,35,59)

result = datetime.timestamp(birthday) # second
result = datetime.fromtimestamp(result)#second to datetime 
result = datetime.fromtimestamp(0)

result = rightnow - birthday # timedelta
# result = result.days
# result = result.seconds
# result = result.microseconds


print( rightnow)
result = rightnow + timedelta(days = 10)
result = rightnow + timedelta(days = 750, minutes=55, seconds=44 )


print(result)



