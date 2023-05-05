'''
print("Hola esto es Python") #con el comando 'print' puedo correr un código

# Operaciones matemáticas
print(12 + 5)
print(15 - 3)
print(12 / 3)
print(2 * 9)
''' 
# Esto es un comentario, no afecta el código y sirve para hacer anotaciones sobre nuestro código.

"""
De esta manera puedo men tar varias líneas de código sin tener que utilizar avrias veces el Hasttag como se puede apreciar en esta misma.

"""

'''
Esta 
    comilla 
           sencilla también nos sirve para el mismo propósito.

'''
# Piedra, Papel o Tijera.

import random

computer_wins = 0
user_wins = 0
rounds = 1

while True:

    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('computer_wins', computer_wins)
    print('User wins', user_wins)

    user_option = input('piedra, papel o tijera ? ')
    print('User ==> ', user_option)
    user_option = user_option.lower()

    
    rounds += 1
    
    omputer_option = ('piedra', 'papel', 'tijera')
    computer_option = random.choice(computer_option)

    if not user_option in computer_option:
        print('ey que pasa vale mia esa no es una opción')
        continue 
        

    print('Computer --> ', computer_option)

    if user_option == computer_option:
        print('its a draw')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('User Wins')
            user_wins += 1
        else:
            print('Computer Wins')
            computer_wins += 1

    elif user_option == 'papel':
        if computer_option == 'tijera':
            print('computer Wins')
            computer_wins += 1
        else:
            print('user Wins') 
            user_wins += 1

    elif user_option == 'tijera':
        if computer_option == "piedra":
            print('computer Wins')
            computer_wins += 1
        else:
            print('user Wins')
            user_wins += 1
    if computer_wins == 2:
        print('The Winner is The Computer ! u Looser ')
        break

    if  user_wins == 2:
        print('The Winner is The User ! u a Champ ! ')
        break

