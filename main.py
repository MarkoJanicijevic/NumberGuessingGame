from functions import *


game_is_on = True

while game_is_on:
    level = choose_level()
    secret_number = generate_random_number()
    print("Welcome to the number guessing game. ")
    print(f"You have {level} attempts to guess secret number between 1 and 100")
    guess_number = int(input("Enter your guess. "))

    while secret_number != guess_number and level > 0:
        compare_numbers(secret_number, guess_number)

        print(f"You have {level} attempts left.")
        guess_number = int(input("Enter another guess. "))
        level -= 1
    if secret_number == guess_number:
        print(f"You have guessed secret number. Secret number is {secret_number}. You have {level} attempts left.")
    else:
        print("You have no more attempts. You loose.")

    choice = input("Do you want to play again? y/n")
    while choice.lower() != "y" and choice.lower() != "n":
        print("Please enter valid input. ")
        choice = input("Do you want to play again? y/n  ")

    if choice.lower() == "n":
        game_is_on = False
    else:
        game_is_on = True


