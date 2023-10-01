# def square(num): return num**2

# numbers =[1,2,5,7]

# result = list(map(square, numbers))

# for item in map(square,numbers):
#     print(item)


# print(result)

# def square(num): return num**2
# square = lambda num:num ** 2 
# numbers =[1,2,5,7]

# # result = list(map(lambda num:num ** 2 , numbers))
# result = list(map(square , numbers))

# # for item in map(square,numbers):
# #     print(item)


# print(result)



numbers =[1,2,5,7,10,4,6]
 
# def check_even(num): return num%2==0
check_even = lambda num:num%2==0 

# result= list(filter(check_even, numbers))
# result= list(filter(lambda num:num%2==0 , numbers))
result= list(filter(check_even, numbers))

print(result)

