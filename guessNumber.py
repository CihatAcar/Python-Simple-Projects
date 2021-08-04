"""
Write a Python program to guess a number between 1 to 9.
Note : User is prompted to enter a guess.
 If the user guesses wrong then the prompt appears again until the guess is correct,
  on successful guess, user will get a "Well guessed!" message, and the program will exit.
  """
import random


def guess_number():
    number = range(1, 10)
    guess = random.choice(number)
    user_guess = int(input("Please guess a number between 1 to 9 : "))
    while user_guess != guess:
        print("Wrong number!")
        user_guess = int(input("Please guess a number between 1 to 9 : "))
    else:
        print("Well guessed!")
        

guess_number()
