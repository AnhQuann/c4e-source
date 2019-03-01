f = open("pg28885.txt")
text = f.read()
f.close()

import string

words = text.replace(",", "").replace(".", "".replace(";", "")).lower().split(" ")
print(words)

dict_count = {}
for word in words:
    if word != "" and word.isalpha():
        if word in dict_count:
            dict_count[word] += 1
        else:
            dict_count[word] = 1























print(dict_count)
