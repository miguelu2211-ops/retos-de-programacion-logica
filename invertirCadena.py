# invertir una cadena sin usar funciones automaticas
texto = "Hola mundo"
texto_invertir =""

for i in range(len(texto) -1, -1, -1):
    texto_invertir += texto[i]
    
print(texto_invertir)