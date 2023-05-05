person = {
    'name': "nico",
    'last_name': "molina",
    'age': 25,
    'langs': ['python', 'JS']
}
print(person)

person['name'] = 'Stivie'
person['age'] -= 50
person['langs'].append('Rust')
print(person)

del person['last_name'] #del me borra del dict.
person.pop('age') #lo mismo
print(person)

print('items => ')
print(person.items())

print('keys => ')
print(person.keys())

print('values => ')
print(list(person.values()))