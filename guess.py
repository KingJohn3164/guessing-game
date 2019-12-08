#this is a Guess the number game
import random

guessesTaken = 0

print('Hello! what is your name?')
myName = input()

number = random.randint(1,20)
print('well,'+ myName +', I am thinking of a number between 1 and 20.')

for guessesTaken in range(6):
    print('Take a guess.') #four spaces in front of "print"
    guess = input()
    guess =int(guess)

    if guess < number:
        print ('your guess is too low') # eight spaces in front of "print"

    if guess > number:
        print ('your guess is too high')
        
    if guess == number:
        break

    if guess == number: 
        guessesTaken = str(guessesTaken + 1)
        print('Good job, '+ myName+ '! you guessed my number in '+ guessesTaken +' guesses!')

        if guess != number:
            number =str(number)
            print('Nope. the number I was thinking of was' + number + '.')