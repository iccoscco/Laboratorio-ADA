# Problema 1
def reverse_polish_notation(cadena):
    # Evaluar la reversión polaca inversa
    pila = []
    arrayCad = cadena.split(" ")

    for i in range(arrayCad):
        if arrayCad[i] != "+" and arrayCad[i] != "-" and arrayCad[i] != "*" and arrayCad[i] != "/":
            
        # else:
        #     n1 = pila.pop()
        #     n2 = pila.pop()
        #     value = 0;
        #     # Revisamos que operación hacer
        #     if auxCad[i] == "+":
        #         value = n1 + n2
        #     if auxCad[i] == "-":
        #         value = n1 - n2
        #     if auxCad[i] == "*":
        #         value = n1 * n2
        #     if auxCad[i] == "/":
        #         value = n1 / n2
        #     pila.append(value)
    print(pila)

reverse_polish_notation("2 1 5 3 *")   
# reverse_polish_notation("2 1 + 3 *")   
# reverse_polish_notation("4 13 5 / +")   