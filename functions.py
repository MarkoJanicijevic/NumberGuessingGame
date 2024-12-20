import random

def choose_level():
    x = input("Choose difficulty level: \n")
    while x != "easy" and x != "hard":
        x = input("Choose difficulty level: \n")
    if x == "easy":
        return 10
    else:
        return 5

def generate_random_number():
    return random.randint(1, 100)

def compare_numbers(x, y):
    if x == y:
        print("You guessed secret number")
    elif x > y:
        print ("Too low")
    else:
        print ("Too high")