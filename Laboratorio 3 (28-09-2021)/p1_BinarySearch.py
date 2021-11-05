# *Problema 1

def binarySearch(array, element):
    # *Realizar el código del binary search
    high = len(array) - 1
    low = 0
    middle = 0
    while low <= high:
        # Evaluación del índice del array
        if len(array) % 2 == 0:
            middle = int((high + low) / 2) + 1
        else:
            middle = int((high + low) / 2)

        # Búsqueda
        if array[middle] == element:
            return middle
        elif element > array[middle]:
            low = middle + 1
        else:
            high = middle - 1
    return -1


# * Casos de prueba
test1 = [2, 8, 45, 76, 89, 90]
test2 = [5, 7, 31, 46, 59]
print(binarySearch(test1, 90))
print(binarySearch(test2, 46))


a = 330
b = 330
print("A") if a > b else print("=")
