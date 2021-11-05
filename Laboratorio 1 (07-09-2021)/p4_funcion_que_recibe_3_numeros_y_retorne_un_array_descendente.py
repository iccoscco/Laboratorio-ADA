# Ejercicio 4
def orderNumbers1(n1,n2,n3): #Solución 1
    array = []
    # Escribir una función que reciba 3 números y retorne un array con los números en orden ascendente
    array.append(n1)
    array.append(n2)
    array.append(n3)
    array.sort()
    return array

def orderNumbers2(n1,n2,n3): #Solución 2
    # Escribir una función que reciba 3 números y retorne un array con los números en orden ascendente
    array = []
    # Al ser 3 números son 6 posibles casos
    if n1 < n2:
        if n2 < n3: 
            array.append(n1)
            array.append(n2)
            array.append(n3)
        else: 
            array.append(n1)
            array.append(n3)
            array.append(n2)
    if n2 < n1:
        if n1 < n3:
            array.append(n2)
            array.append(n1)
            array.append(n3)
        else:
            array.append(n2)
            array.append(n3)
            array.append(n1)
    if n3 < n1:
        if n1 < n2:
            array.append(n3)
            array.append(n1)
            array.append(n2)
        else:
            array.append(n3)
            array.append(n2)
            array.append(n1)
    return array

# Casos de prueba
test1 = orderNumbers1(78,23,60)
test2 = orderNumbers2(12,56,23)
print(test1)
print(test2)

# Una tercera forma sería usando algoritmos de ordenación como bubbleSort, mergeSort, etc, no los usé porque en este caso solo pide 3 números