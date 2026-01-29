# Dice rolling game

import random
dice_numbers = [1, 2, 3, 4, 5, 6]
dice_numbers_two = [1, 2, 3, 4, 5, 6]


print("welcome to the dice rolling game!")
while True:
    user_input = input("Choose (y/n): ")
    if user_input.lower() == "y":
        print("Rolling the dice...")
        print(
            f"you rolled a {random.choice(dice_numbers)} and a {random.choice(dice_numbers_two)}")

    elif user_input.lower() == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input!, Please choose either y or n")
