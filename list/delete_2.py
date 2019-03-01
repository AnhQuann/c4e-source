favs = ['death note', 'netflix', 'teaching']
print("Hi there, here you favorite things so far")

print("**************************************")
for index, fav in enumerate(favs):
    print(index + 1, '.', fav)
print("**************************************")

fav = input("Favorite stuff you want to get rid of?")
favs.remove(fav)

print("**************************************")
for index, fav in enumerate(favs):
    print(index + 1, '.', fav)
print("**************************************")
