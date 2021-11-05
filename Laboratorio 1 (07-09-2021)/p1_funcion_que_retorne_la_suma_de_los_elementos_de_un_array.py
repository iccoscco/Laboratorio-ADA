# Ejercicio 1
def sumArray1(array): #* Solución 1
    # Escribir una función que tenga como parámetro de entrada un array y retorne la suma de los mismos
    return sum(array)

def sumArray2(array): #* Solución 2
    # Escribir una función que tenga como parámetro de entrada un array y retorne la suma de los mismos
    suma = 0
    for i in array:
        suma += i
    return sum(array)

# Caso de prueba
arr = [1,2,3,4,5,6,7,8,9,10]
test1 = sumArray1(arr)
test2 = sumArray2(arr)
print(test1)
print(test2)