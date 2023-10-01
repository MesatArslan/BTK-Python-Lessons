name = 'Mahmut'
surname = 'Arslan'
age = 45


print('My name is {}'.format(name))
print('My name is {} {}'.format(name, surname))
print('My name is {1} {0}'.format(name, surname))
print('My name is {l} {b}'.format(b=name, l=surname))
print("My name is {} {} and I'm {} years old.".format(name, surname, age))

result = 200/ 700
print('The result is {}'.format(result))
print('The result is {r:1.3}'.format(r=result))
print('The result is {r:10.3}'.format(r=result))

print(f"My name is {name} {surname} and I'm {age} years old.")

