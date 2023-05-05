text = 'Ella sabe programar en Python'
'''
print('JavaScript' in text) #in busca en el texto
print('Python' in text)

if 'Python' in text:
    print('Elegiste bien')
else:
    print('Also you chose good ma G!')
'''
size = len(text) #les() cuántos caracteres tiene
print(size)
print(text)
print(text.upper()) #.upper() pasa todo a Mayus.

print(text.lower()) #.lower() todo a minu.
print(text.count('a')) #.count('') cuantas veces esta una letra en el texto

print(text.swapcase()) #mayus a minus y viceversa.
print(text.startswith('Ella')) #si empieza por:
print(text.endswith('Rust')) #finaliza por:
print(text.replace('Python', 'Go')) #nos cambia texto

text_2 = 'este es un titulo'
print(text_2)
print(text_2.capitalize()) #pone primer caracter en mayus.
print(text_2.title()) #inicio de cada palabra en mayus
print(text_2.isdigit()) # nos dice si el texto es un digito
print('398'.isdigit())