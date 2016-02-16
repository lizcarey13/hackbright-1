# Create a file called guess_number.py in ~/intro_class. Inside this file, 
# create a program that uses Python to generate a random number between 1 and 10 
# and store it in a variable. Prompt the user to guess the number. If their guess 
# is too high, print "too high!" And allow the user to guess again. If their guess 
# is too low, print "too low!" And allow the user to guess again. If their guess 
# is equal to the computer's number, print "you win!" And exit the program. 

# Modify this program to allow the user to pick the upper bound on the range for the game. 
# E.g. 1-50 instead of 1-10
import random

def guess_game():
    rand_number = random.randint(1, 10) 

    while True:
        guess = int(raw_input("Enter your guess from 1 to 10: "))

        if guess > rand_number:
            print "too high! Try Again: "
        elif guess < rand_number:
            print "too low! Try Again: "
        else:
            print "you win!"
            break

guess_game()

def guess_game_with_upper(upper_bound):
    rand_number = random.randint(1, upper_bound) 

    while True:
        guess = int(raw_input("Enter your guess from 1 to " + str(upper_bound) + ": "))

        if guess > rand_number:
            print "too high! Try Again: "
        elif guess < rand_number:
            print "too low! Try Again: "
        else:
            print "you win!"
            break

guess_game_with_upper(50)
