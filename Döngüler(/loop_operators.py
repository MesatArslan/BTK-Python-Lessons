# range
# for item in range(50,101,5):
#     print(item)

# print(list(range(5,100,10)))


# enumerate

# greeting = 'Hello There'
# index = 0
# for letter in greeting:
#     if letter == ' ':
#       continue
#     print(f'index:{index} letter: {letter}')
#     index += 1

#  

# greeting = 'Hello'
# for item in enumerate(greeting):
    
#  print(item)



# zip


# list1 = [1,2,3,4,5]
# list2 = ['a','b','c','d','e']
# list3 = [100,200,300,400,500]

# print(list(zip(list1,list2)))
# print(list(zip(list1,list2,list3)))


list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]


# for item in zip(list1,list2,list3):
#     print(item)

for a,b,c in zip(list1,list2,list3):
 print(a)