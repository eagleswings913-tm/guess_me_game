
from random import randint

lower = 1
higher = 10

rand_num = randint(int(lower),int(higher))

while True:
    guess = int(input(f'Enter a number between {lower} and {higher}: '))
    if guess >= lower and guess <= higher:
        if guess == rand_num:
            print('Success')
            break
        else:
            print('Try again')
            
print('You are a genius!')
