"""guess the number in my mind"""

import random


secret_number = random.randint(1, 10)
guess_number = int(input())
counts = 1
while guess_number != secret_number:
    if guess_number > secret_number: 
        print('Too high!')
    else:
        print('Too low!')
    counts += 1
    guess_number = int(input())

print(f'correct! That is the number in my mind.\nYou guess {counts} times totally.')