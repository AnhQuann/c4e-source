favs = ['death note', 'netflix', 'teaching']
print("Hi there, here you favorite things so far")

print(50 * "*")
for index, fav in enumerate(favs):
    print("{0}. {1}".format(index + 1, fav))
print(50 * "*")

index = int(input("Position you want to update?")) - 1
fav = input("Your replacing favorite?")
favs[index] = fav

print(50 * "*")
for index, fav in enumerate(favs):
    print("{0}. {1}".format(index + 1, fav))
print(50 * "*")
