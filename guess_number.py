#info: A game base on your luck by guessing random number and win.
import random

n = int(input("Please pick a number from 1 to 10: "))
numbers = random.randint(1,10)

if n == numbers:
    print("Congratulations, You won!")
else: #why else? If it not the right number then everything false.
    print("Oh, Better luck next time!")