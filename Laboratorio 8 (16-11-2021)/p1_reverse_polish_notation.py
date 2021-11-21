# Problema 1
def reverse_polish_notation(cadena):
    # Evaluar la reversión polaca inversa
    pila = []
    for i in range(0,len(cadena),2):
        if cadena[i] != "+" and cadena[i] != "-" and cadena[i] != "*" and cadena[i] != "/":
            pila.append(int(cadena[i]))

    print(pila)





reverse_polish_notation("3 + 5")   