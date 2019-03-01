person = {
    'name': 'Tuấn Anh',
    'age': 22,
    'exs': 3
}

person['home'] = 'Mộc Châu'

print(person)

del person['age']

print(person)

for key, value in person.items():
    print(key, value)

print(list(person.keys()))
