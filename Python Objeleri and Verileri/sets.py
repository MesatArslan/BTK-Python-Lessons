fruits = { 'banana', 'apple', 'orange'}

# print(fruits[0]) non-indexable list.

for x in fruits:
    print(x)

fruits.add('cherry')
fruits.update(['mango', 'grape', 'apple'])
fruits.remove('mango')
# fruits.clear()
print(fruits)


myList = [1,2,4,4,5,2,1]

print(set(myList))