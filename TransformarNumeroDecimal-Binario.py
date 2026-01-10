def decimal_a_binario(n):
    if n == 0:
        return "0"

    binario = ""
    while n > 0:
        residuo = n % 2
        binario = str(residuo) + binario
        n //= 2

    return binario

# Ejemplo
numero = 3
print(decimal_a_binario(numero))
