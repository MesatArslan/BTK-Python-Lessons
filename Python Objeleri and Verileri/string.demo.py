website = "https://www.sadıkturan.com"
course = "Python Course: Baştan sona python programlama rehberiniz.(40 hours)"

print(len(course))
print(website[8:11])
print(website[-3:])

a=course[:15]
b=course[-15:]
print(a,b)
print(course[::])
print(course[::1])
print(course[::2])
print(course[::3])
print(course[::-1])

s = '12345' *5
print(s)
print(s[::5])


name = 'Bora'
surname = 'Yılmaz'
age = 36
job = 'Mühendis'

print(f"My name is {name} {surname}, my age is {age} and I'm {job}")

d= 'abc ' *3
print(d)

s = 'Hello world'       # w yü W ile değiştir
# s = s[:6] +'W' + s[-4:]
# print(s)
s = s.replace('w', 'W')
print(s)
