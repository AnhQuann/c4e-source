low = 1
high = 101
loop = True

print("Guess your number game")
input("Now think of a number from 0 to 100, then press 'Enter'")
print("All you have to do is to answer to my guess")
print("'c' if my guess is 'C'orrect")
print("'s' if my guess is 'S'maller than your number")
print("'l' if my guess is 'L'arger than your number")

while loop:
    mid = (high + low) // 2
    answer = input("Is {0} your number?".format(mid))
    if answer.lower() == 'c':
        print("I knew it")
        loop = False
    elif answer.lower() == 's':
        low = mid
    elif answer.lower() == 'l':
        high = mid
