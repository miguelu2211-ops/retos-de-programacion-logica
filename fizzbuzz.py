# Reto FizzBuzz
# Mostrar numeros de 1 al 100
# Multiplos de 3 -> fizz
# Multiplos de 5 -> buzz
# Multiplos de 3 y 5 -> fizzbuzz

for numero in range(1,100):
    if numero % 3 == 0 and numero % 5 == 0:
        print("fizzbuzz")
    elif numero % 3 == 0:
        print("fizz")
    elif numero % 5 == 0:
        print("buzz")
    else:
        print(numero)