'''
1-Try to find the number to be randomly generated between 1-100 with the following expressions.(life = 5)
***Search for 'Random Python' for the random module.
***Score out of 100, each question is 20 points.
***Get the right informations from the users and each question will be calculated over the specific number of lives.

'''

import random

number = random.randint(1,10)

life = int(input('How many life do you want?: '))
right = life
counter = 0
while right > 0:
    right -= 1
    counter += 1
    guess = int(input('Guess: '))

    if guess == number:
        print(f'Congratulations, You found on the {counter}. time. Total point: {(100) - (100/life) * (counter - 1 )}')
        break
    elif number > guess:
        print('!Go up!')
    else:
        print('!Go down!')
    
    if right == 0:
        print(f'Life is over. Guess number: {number}. Your point is: 0')





