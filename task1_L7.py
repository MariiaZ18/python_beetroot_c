# The Guessing Game.
# Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.

import random


def guessing_game():
    ramdom_number = random.randint(0, 10)
    while True:
        enter_number = int(input("Enter integer from 0 to 10: "))
        if enter_number == ramdom_number:
            print("Congratulations! You guessed it!")
            break
        elif enter_number < ramdom_number:
            print("Your number is less")
        elif enter_number > ramdom_number:
            print("Your number is higher")


if __name__ == '__main__':
    guessing_game()
