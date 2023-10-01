# def cube():
#     for i in range(500):
#         yield i ** 3 
# # iterator = cube()
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))
 

# for i in cube():
#     print(i)



generator= (i**3 for i in range(5))
print(generator)


for i in generator:
    print(i)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
