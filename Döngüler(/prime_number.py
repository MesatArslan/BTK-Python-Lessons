'''
Question:Find whether a given number is prime or not.
*** A prime number is a number that has no divisors other than 1 and itself.

'''

Number = int(input('Number: '))
prime = True

if Number == 1 :
    print('1 is not an prime number.')
for i in range(2,Number):
    if (Number % i == 0):
        prime = False
        break

if prime:
    print(f'{Number} is prime number.')
