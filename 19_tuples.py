numbers = (1, 2, 3, 5)
strings = ('stivie', 'Mateo', 'laura', 'stivie')
print(type(numbers))
print('0 => ', numbers[0])
print('-1 => ', numbers[-1])
print(numbers, strings)
print(type(strings))

# tuplas son inmutables, no se peuden modificar.

print(strings)
print(strings.index('Mateo'))
print(strings.count('stivie')) #.count me dice cuantas veces esta el elemento

my_list = list(strings) #list(), pasamos de tupla a list
print(type(my_list))
print(my_list)

my_tuple = tuple(my_list) #tuple, me lo comvierte a tuple
print(my_tuple)