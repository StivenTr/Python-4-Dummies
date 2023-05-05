text = 'Ella sabe Python'
print(text[0]) #me muestra caracter en esa posicion
print(text[1])
###print(text[999])
size = len(text)
print('size => ', size)
print(text[size - 1]) # para hallar el último caracter de la posición, - 1 ya que empieza desde 0.

print(text[-1]) #lo mismo pero màs fácil, empieza a contar hacias atars.

# slicing

print(text[0:5])
print(text[10:16])
print(text[:10])
print(text[5:-1])
print(text[5:])
print(text[:])
print(text[10:16:1]) #salto entre caracteres
print(text[10:16:2]) # me muestra los pares de Python cada 2 saltos pto.
print(text[::2])