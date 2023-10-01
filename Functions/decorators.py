def my_decorator(func):
    def wrapper(name):
        print('process before the functions')
        func(name)
        print('process after the functions')
    return wrapper

# @my_decorator
# def sayHello(name):
#     print('hello', name)

#      finish = time.time()
#     print("fonksiyon" + str(finish-start) + "saniye sürdü.")
# sayHello("Ali")


import math
import time
def calculate_time(func):
        def inner(*args,**kwargs):
            start = time.time()
            time.sleep(1)
            
            func(*args,**kwargs)
            finish = time.time()
            print("fonksiyon"+" "+ func.__name__ +" "+ str(finish-start) + " "+"saniye sürdü.")
        return inner
@calculate_time
def usalma(a,b):
   print(math.pow(a,b))
     
@calculate_time
def factorial(num):
    print(math.factorial(num  ))

@calculate_time
def collection(a,b):
     print(a+b)
    
usalma(2,3)
factorial(4)
collection(10,20)