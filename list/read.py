favs = ['death note', 'netflix', 'teaching']
print("Hi there, here you favorite things so far")

print("**************************************")
print(*favs, sep=', ')
print("**************************************")
for index, fav in enumerate(favs):
    print(index + 1, '.', fav)
print("**************************************")
