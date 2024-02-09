#info: A game base on your luck by guessing random number and win.
import random
n = int(input("Please pick a number from 1 to 10: "))
rand = random.randint(1,10)
num = rand
while n != num:
    if n < num:
        print("Your number is too low! Try again\n")
        n = int(input("Please pick a number from 1 to 10: "))
    elif n > num:
        print("Your number is too high! Try again\n")
        n = int(input("Please pick a number from 1 to 10: "))
    else:
        break
print("Congratulations, You won!")