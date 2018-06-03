def square(x): #def potem nazwa funkcji w nawiasach specyfikacja argumentów
    return x ** 2 #zwraca kwadrat

y = square(3) #lub square(x=3)
print(y)

def power(exponent, base):
    return base ** exponent

print(power(2, 3))
print(power(exponent = 2, base = 3))

print(power(base = 3, exponent = 2)) #można zamienić kolejność jedynie przy podawaniu argumentów przez nazwę
print(power(2, base = 3)) #odwrotnie się nie da tzn power (3, exponent=4)
