# Problema 1
def reverse_polish_notation(cadena):
    # Evaluar la reversión polaca inversa
    pila = []
    arrayCad = cadena.split(" ")

    for i in range(len(arrayCad)):
        if arrayCad[i] != "+" and arrayCad[i] != "-" and arrayCad[i] != "*" and arrayCad[i] != "/":
            pila.append(int(arrayCad[i]))
        else:
            n2 = pila.pop()
            n1 = pila.pop()
            value = 0;
            # Revisamos que operación hacer
            if arrayCad[i] == "+":
                value = n1 + n2
            if arrayCad[i] == "-":
                value = n1 - n2
            if arrayCad[i] == "*":
                value = n1 * n2
            if arrayCad[i] == "/":
                value = n1 / n2
            pila.append(int(value))
    print(pila)
 