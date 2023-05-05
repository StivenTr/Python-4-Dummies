my_dict = {}
print(type(my_dict))

my_dict = {
    'name': 'stiven',
    'last_name': 'trujillo',
    'age': 28
}
print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('age')) #me da el valor de 'age'
print(my_dict.get('algo')) #lo mismo pero me devuelve un 'none' no esta y no me devuelve une rror

print('avion' in my_dict)

