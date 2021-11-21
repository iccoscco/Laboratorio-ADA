# Problema 2:

def minimun_size_valid(cadena):
    # Determinar cuantos paréntesis válidos se ingresan al programa
    pila = []
    for i in range(len(cadena)):
        # Revisar su la pila contiene elementos o no
        if len(pila) > 0:
            print(f"{pila} =======")
            if pila[len(pila)-1] != cadena[i] and cadena[i] == ")":
                pila.pop()
            else:
                pila.append(cadena[i])

        else: 
            pila.append(cadena[i])
    print(len(pila))

# Casos de prueba
minimun_size_valid("())")
minimun_size_valid("(()))(")
minimun_size_valid("(((")
minimun_size_valid("()))((")
