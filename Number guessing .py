import random

num = random.randint(1, 50)

while True:
    guess = int(input("Guess: "))
    if guess == num:
        print("You won!")
        break
    elif guess < num:
        print("Too low")
    else:
        print("Too high")
