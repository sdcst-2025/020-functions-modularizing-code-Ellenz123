"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""
import random

def title():
    print("This is a number guessing game.")
    print("Enter a number between 1 and 20 in order to guess the secret number!")

title()

def game():
    number=random.choice(range(1,20))
    while True:
        try:
             guess=input("Enter an integer between 1 and 20:")
             guess=int(guess)
             if guess== number:
               print("Congratulations! That is the right number!")
               break
             elif guess< number:
                  print("Try a larger number.")
             else:
                 print("Try a smaller number.")
        except:
            print("Enter a valid integer.")
        
game()