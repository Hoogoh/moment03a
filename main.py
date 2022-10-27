"""""
CorrectUsername = 'Hugo'
CorrectPassword = 'Hugo'

username = input('Write your username here: ')
if username == CorrectUsername:
    password = input('Write your password here: ')
    if password == CorrectPassword:
        print('Access Granted')
"""""

import random

guess_made = 0

name = input('Hello there! What shall I call you?\n')

number = random.randint(0, 10)
print('Well, {0}, I am thinking of a number between 0 and 10000.'.format(name))

while guess_made < 10:

    guess = int(input('Take a guess: '))

    guess_made += 1

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    print('Good job, {0}! You guessed my number in {1} guesses!'.format(name, guess_made))
else:
    print('Nope. The number I was thinking of was {0}'.format(number))
