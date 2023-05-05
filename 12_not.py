print(not True)
print(not False)


print('NOT AND') 
print('not True and True => ', not (True and True))
print('not True and False => ', not (True and False))
print('not False and True => ', not (False and True))
print('not False and False => ', not (False and False))

stock = input("Ingrese el # de stock -> ")
stock = int(stock)

print(not (stock >= 100 and stock <= 1000))