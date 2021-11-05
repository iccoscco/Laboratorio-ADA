# Ejercicio 2
def invertArray1(array): # Solución 1
    # Escribir una función que tenga como parámetro de entrada un array y retorne un array en orden inverso
    array = array[::-1]
    return array

def invertArray2(array): # Solución 2
    # Escribir una función que tenga como parámetro de entrada un array y retorne un array en orden inverso
    arrInv = []
    for i in range(len(array)-1,-1,-1):
        arrInv.append(array[i])
    return arrInv

# Caso de prueba
arr = [2,4,6,8]
test1 = invertArray1(arr)
test2 = invertArray2(arr)
print(test1)
print(test2)