# CRUD create, read, update & delete.

numbers = [1, 2, 3, 4, 5]
print(numbers[1])
numbers[-1] = 10
print(numbers)

numbers.append(700) #.append em agrega al ultimo
print(numbers)

numbers.insert(0, 'hola') #.insert me agrega en la posicion selecionada
print(numbers)

numbers.insert(3, 'change')
print(numbers)

tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + tasks
print(new_list)

index = new_list.index('todo 2') #.index me dice la posiciond e lo que estoy buscando
new_list[index] = 'todo change'
print(new_list)

new_list.remove('todo 1') #.remuve remueve literal
print(new_list)

new_list.pop() #.pop me elimina el ultimo ele. de la lista
print(new_list)

new_list.pop(0)
print(new_list)

new_list.reverse() #.reverse me cambia el orden
print(new_list)

numbers_a = [1, 3, 6, 8, 2, 0]
print(numbers_a)
numbers_a.sort() #.sort me ordena
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)

