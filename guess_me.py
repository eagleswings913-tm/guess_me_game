
from random import randint

min_range = 1
max_range = 100
user_guess = 0
max_guesses = 10
number_of_guesses = 0
play_again = True
continue_play = 'y'

def generate_random_integer(lower_limit, upper_limit):
    return randint(lower_limit, upper_limit)

while play_again:
    random_number = generate_random_integer(min_range, max_range)
    number_of_guesses = 0
    while number_of_guesses < max_guesses:
        try:
            user_guess = int(input(f'Please enter your guess: (number  {min_range} - {max_range}): '))
            if min_range <= user_guess <= max_range:
                number_of_guesses += 1
                if user_guess < random_number:
                    print(f'Your guess is TOO LOW! Try a larger number')
                elif user_guess > random_number:
                    print(f'Your guess is TOO HIGH! Try a smaller number')
                else:
                    print(f'Congratulations, your guess is CORRECT! It took {number_of_guesses} guesses!')
                    break
            else:
                print(f'Error: Number must be between {min_range} and {max_range}, try again!')
        except ValueError:
            print(f'Error: Please enter a number between {min_range} and {max_range}, try again!')
    else:
        print(f'The answer is {random_number}. Better luck next time!')
    while True:
        continue_play = input('Do you want to play again? (y/n): ')
        if continue_play not in ['y', 'n']:
            print('Please enter yes ("y") or no ("n")')
        elif continue_play == 'n':
            play_again = False
            break
        else:
            break
print('Thank you for playing!')