x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6

#1-What is the diffrence between the product of the two numbers you receive from the user and the sum of x,y,z?

# a = int(input("1.sayı: "))
# b = int(input("2.sayı: "))

# result = (a*b)-(x+y+z)

# print(result)

#2-Calculate the quotient of y without a remandier of x
# result = y // x

#3-What is mod3 of (x, y, z) sum.
toplam = (x+ y+ z)
result = toplam % 3 
#4-Calculate the xth power of y.

result = y ** x
#5-What is the cube of z according to operation x, *y, z= numbers.

x, *y, z= numbers
result = z ** 3
#6-What is the sum of y values according to operation x, *y, z= numbers.

x, *y, z= numbers
result= y[0] + y[1]+ y[2]




print(result)