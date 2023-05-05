name = "Stiven"
Last_name = "Trujillo"
print(name)
print(Last_name)

# Concatenación '+'

full_name = name + " " + Last_name
print(full_name)

quote = "I a'm Stiven"
print(quote)

quote2 = " She said: 'Hello ma G !'"
print(quote2)


# format, es una forma en python de darle estructura al texto.

template = "Hola, mi nombre es " + name + ", y mi apellido es " + Last_name
print("v1 ", template)

template = "Hola, mi nobre es {} y mi apellido es {}".format(name, Last_name)
print("v2 ", template)

template = f"Hola, mi nombre es {name} y mi apellido es {Last_name}"
print("v3", template)

age = 28

template = f"Hola, mi nombre es {name} {Last_name} y tengo {age} años"
print("v4", template)