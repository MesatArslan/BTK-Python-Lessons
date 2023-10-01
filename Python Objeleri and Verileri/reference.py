# value types => string,number

x = 5

y = 25               #    value değer tipinde y'de yapılan bir değişiklik x'i etkilemez

x = y

y=10

# print(x,y)

#referance types => list

a = ["apple", "banana"]
b = ["apple", "banana"]

a = b

b[0]="grape"

print(a,b)