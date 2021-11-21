# Problema 4:
import collections
def backspace(cadena):
# Cuando se presione la tecla numeral se borraran los datos de entrada
    cola = collections.deque([])
    for i in range(len(cadena)):
        if cadena[i] == "#":
            cola.pop()
        else:
            cola.append(cadena[i])

    print(cola)



# Casos de prueba
str = "abc#de##f#ghi#jklmn#op#"
backspace(str)