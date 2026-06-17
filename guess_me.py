
from random import randint

lower = 1
higher = 10

rand_num = randint(int(lower),int(higher))

while True:
    try:
        guess = int(input(f'Enter a number between {lower} and {higher}: '))
        if lower <= guess <= higher:
            if guess == rand_num:
                print('Success')
                break
            else:
                print('Try again')
        else:
            print(f'Number must be between {lower} and {higher}, try again!')
    except ValueError:
        print('Please enter a number')
            
print('You are a genius!')
