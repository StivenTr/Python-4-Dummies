name = "Stiven"
print(type(name))
name = 15
print(type(name))
name = True
print(type(name))

age = 12
print('Mi edad es ' + str(age))
# "str" volvemos el entero a un string
print(f"Mi edad es {age}")


age = input('Cuál es tu edad ->') #input siempre nos va a devolver un "str"
print(type(age), age)
age = int(age)
age += 10
print(f"Tu edad en 10 años será: {age}")
