x = 3.3
y = 1.1 + 2.2
print(x)
print(y)
print(x == y) #False

y_str = format(y, '.2g')
print(y_str)
print(x == y) # False porque quedo como formato str
print(y_str == str(x))


print('*' * 10)

print(y, x)

tolerance = 0.00001
print(abs(x - y) < tolerance) #abs Valor absoluto para que de + 
