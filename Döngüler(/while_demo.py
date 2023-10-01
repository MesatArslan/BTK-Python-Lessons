numbers = [1,3,5,7,9,11,12,19,21]

#1-Print the list of numbers with a while loop.
# i = 0

# while (i < len(numbers)):
#     print(numbers[i])
#     i +=1

#2-Take the start and end numbers from the user and print all the odd numbers in between.

# start = int(input('Starting number: '))
# end= int(input('Ending number: '))

# i = start
# while i < end:
#     i += 1
#     if (i % 2 == 1):
#      print(i)
    
#3-Print numbers 1-100 in descending order.

# i = 100

# while i > 0:
#     i -=1
#     print(i)
    
#4-Print the 5 numbers you will receive from the user, in order.

# numbers = []

# i = 1

# while i < 6 : 
#     num = int(input(f'Number{i}:'))
#     numbers.append(num)
#     i += 1
# numbers.sort()
# print(numbers)
   




#5-Store the unlimited product information you will receive from the user in the list of products.

products = [ ]

i = 1
numprod = int(input('Product number: '))

while (i <= numprod):

    product = str(input(f'Product{i} name: '))
    price = float(input(f'Product{i} price: '))

    products.append(
        {'name' : product , 'price': price}
          )
       
    i +=1
for nam in products:
 print(f'Product name: {nam ["name"]} Product price: {nam ["price"]}')



# ***Ask the user for number of product.
# ***Let the dictionary list structure be(name, price).
# ***When the product adding proccess is finished, list the products with while.

