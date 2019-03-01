favs = ['death note', 'netflix', 'teaching']
print("Hi there, here you favorite things so far")

print("**************************************")
for index, fav in enumerate(favs):
    print(index + 1, '.', fav)
print("**************************************")

index = int(input("Favorite position you want to get rid of? ")) - 1
favs.pop(index)

print("**************************************")
for index, fav in enumerate(favs):
    print(index + 1, '.', fav)
print("**************************************")
