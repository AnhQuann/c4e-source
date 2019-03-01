### - Array indexing (use index to access situational data)
### - Searching
### - Counting
### - Place variable outside scope
statuses = [
"""
 _________
 |        |
 |        O
 |
 |
 |
_|_
""",
"""
 _________
 |        |
 |        O
 |        |
 |
 |
_|_
""",
"""
 _________
 |        |
 |        O
 |       -|
 |
 |
_|_
""",
"""
 _________
 |        |
 |        O
 |       -|-
 |
 |
_|_
""",
"""
 _________
 |        |
 |        O
 |       -|-
 |       /
 |
_|_
""",
"""
 _________
 |        |
 |        O
 |       -|-
 |       / \\
 |
_|_
"""
]

words = {
    'awkward': 'causing or feeling embarrassment or inconvenience.',
    'microwave': 'a wave, used in cooking',
    'vodka': 'alcohol, russian origin'
}

from random import choice
word = choice(list(words.keys()))
characters = list(word)
display_text = list("_" * len(word))
word_hit_count = 0
guess_left = len(statuses)

loop = True

while loop:
    print(*display_text, sep = " ")
    guess = input("Your guess?")
    found = False
    for index, char in enumerate(characters):
        if char == guess:
            display_text[index] = char
            word_hit_count += 1
            found = True
    if not found:
        guess_left -= 1
        if guess_left == 0:
            print("You lost")
            loop = False
        else:
            print(statuses[-guess_left])
    elif word_hit_count == len(characters):
        loop = False
        print("You won")
