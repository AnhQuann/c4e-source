from random import choice
word = choice(['champion', 'dungeon', "vodka", "canada"])
chars = list(word)
while len(chars) > 0:
    import random
    c = random.choice(chars)
    chars.remove(c)
    print(c, end = ' ')
print()

answer = input("Your answer: ")
if answer == word:
    print("Hura")
else:
    print(":(")
