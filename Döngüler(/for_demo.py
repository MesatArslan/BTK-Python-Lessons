numbers = [1,3,5,7,9,12,19,21]

#1-Which numbers in the list of numbers are a multiple of 3?

# for num in numbers:
#    if (num %3 ==0):
#      print(num)
  

#2-What is the sum of the numbers in the list of numbers?
# sum1 = 0
# for num in numbers:
#     sum1 += num
# print('sum:', sum1)

#3-Square the odd numbers in the list of numbers?

# for num in numbers:
#     if ( num % 2 ==1):
#         print(num **2)



cities = ['Kocaeli', 'Istanbul', 'Ankara', 'Izmir', 'Rize']

#4-Which cities have at most 5 letters?

# for city in cities:
#     if (len(city) <= 5):
#       print(city)

products= [
    {'name':'Samsung 3','price':'3000'},
    {'name':'Samsung 4','price':'5000'},
    {'name':'Samsung 5','price':'7000'},
    {'name':'Samsung 7','price':'9000'},
    {'name':'Samsung 9','price':'11000'}
]

#5-What is the total price of products?
# sum1 = 0
# for product in products:
#     sum1 += int(product['price'])
# print(sum1)





#6-Show the products with a maximum price of 7000 products.
sum1 = 0
for product in products:
    if int(product['price']) <7000:
        print(product['name'])