# def ChangeName(n):
#     n = 'Ada'

# name = 'Mehmet'

# ChangeName(name)
# print(name)

# def change(n):
#     n[0] = 'Istanbul'

# cities = ['Ankara', 'İzmir']
# n = cities[:]

# n[0] = 'Istanbul'
# print(cities)

# def add(*params):
#     print(params)
#     return sum(params)

# print(add(10,20))
# print(add(10,20,550,70))
# print(add(178,200))


def displayusers(**args):
    print(type(args))
    for key,value in args.items():
         print('{} is {}'.format(key,value))



displayusers(name= 'Cinar', age = 2 , city = 'Istanbul')
displayusers(name= 'Mehmet', age = 25 , city = 'Ankara', phone= 5344444,)
displayusers(name= 'Demir', age = 78 , city = 'Mekke', phone= 534464, email=  'tartar@gmail.com')


def myFunc(a,b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50, key1= 'value1', key2= 'value2')