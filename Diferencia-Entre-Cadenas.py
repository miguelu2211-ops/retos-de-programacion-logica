def encontrar_diferencias(str1, str2):
    # out1: Caracteres en str1 que NO están en str2
    out1 = "".join([char for char in str1 if char not in str2])
    
    # out2: Caracteres en str2 que NO están en str1
    out2 = "".join([char for char in str2 if char not in str1])
    
    print(f"out1: {out1}")
    print(f"out2: {out2}")

# Ejemplo de uso
encontrar_diferencias("Pelotas", "Balones")