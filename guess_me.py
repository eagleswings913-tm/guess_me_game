
import sys
from random import randint
print('I am in')

#print(sys.argv[0])
#print(sys.argv[1])
#print(sys.argv[2])


#lower = sys.argv[1]
#higher = sys.argv[2]

lower = 1
higher = 10

rand_num = randint(int(lower),int(higher))

#print(rand_num)

while True:
    guess = int(input(f'Enter a number between {lower} and {higher}: '))
    if guess >= lower and guess <= higher:
        if guess == rand_num:
            print('Success')
            break
        else:
            print('Try again')
            
print('You are a genius!')


# cd /storage/3037-3961/Python