'''
    Circle Area   : πr²
    Circle Around : 2π
    * Yariçapi verilen dairenin alan ve çevresini hesaplayiniz.
    π(3.14)
'''
pi = 3.14
r = float(input('Radius: '))
circleArea = pi * r**2
circleAround = 2 * pi * r

 # print('Circle Area:',circleArea)
 # print('Circle Around:',circleAround)

print("Area:"+ str(circleArea) + " "+" Around:" + str(circleAround))

