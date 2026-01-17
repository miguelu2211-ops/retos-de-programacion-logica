n1 = float(input("156: "))
n2 = float(input("267: "))
n3 = float(input("456: "))

if n1 == n2 == n3:
    print("Los tres números son iguales.")
elif n1 >= n2 and n1 >= n3:
    print(f"El número mayor es: {n1}")
elif n2 >= n1 and n3 >= n3:
    print(f"El número mayor es: {n2}")
else:
    print(f"El número mayor es: {n3}")
