# and
print('AND') # Condición
print('True and True => ', True and True)
print('True and False => ', True and False)
print('False and True => ', False and True)
print('False and False => ', False and False)

print("-----" * 5)
print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)

print("-----" * 5)

stock = input("Ingrese el # de stock -> ")
stock = int(stock)

print(stock >= 100 and stock <= 1000)

print("-----" * 5)
# or
print('OR') # si alguno de los dos es T la eje. será True
print('True or True => ', True or True)
print('True or False => ', True or False)
print('False or True => ', False or True)
print('False or False => ', False or False)

role = input("Digite el rol => ")
print(role == "admin" or role == "seller")
