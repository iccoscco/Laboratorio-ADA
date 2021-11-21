# Problema 1
def reverse_polish_notation(cadena):
    # Evaluar la reversión polaca inversa
    pila = []
    arrayCad = cadena.split(" ") # Transformación de cadena en array

    for i in range(len(arrayCad)):
        # Verificación de que elemento se está mandando
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
 

# Casos de prueba
reverse_polish_notation("2 1 + 3 *")   
reverse_polish_notation("4 13 5 / +")  
reverse_polish_notation("10 6 9 3 + -11 * / * 17 + 5 +")  
