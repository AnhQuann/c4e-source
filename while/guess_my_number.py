import random

n = random.randrange(1, 101)
loop = True

while loop:
    guess = int(input("Guess my number (1-100)? "))
    if guess == n:
        print("Bingo")
        loop = False
    elif guess > n:
        print("A little too large :(")
    else:
        print("Too small :(")
