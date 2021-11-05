# Ejercicio 3
def evenAndOddNumber(array):
    # Escribir una función que tenga como parámetro de entrada un array y retorne dos arrays con los números separados pares e impares
    arrEven = []
    arrOdd = []
    for i in array:
        if i%2 == 0:
            arrEven.append(i)
        else:
            arrOdd.append(i)
    print(f"Números pares: {arrEven}")
    print(f"Números impares: {arrOdd}")
    
# Caso de prueba
arr = [12,55,7,8,90,34,2,4,1]
evenAndOddNumber(arr)
