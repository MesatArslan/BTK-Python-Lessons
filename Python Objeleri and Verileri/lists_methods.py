numbers = [1,15,25,10,65,4,7,10]
letters = ['a', 'g', 's', 't', 'i', 's', 'a']

val = min(numbers)
val = max(numbers)
val = min(letters)
val = max(letters)

val = numbers[3:6]
val = numbers[:4]

numbers.append(49)
numbers.insert(3, 78)
numbers.pop(0)
numbers.remove(49)

numbers.sort()
letters.sort()

numbers.reverse()
letters.reverse()

print(numbers)
print(letters)

print(len(numbers))
print(len(letters))
print(numbers.count(10))
print(letters.count('a'))
print(letters.count(' '))

numbers.clear()
print(number)
