# Problema 5 

# Ordenamiento por inserción
def insertionSort(array):
    for i in range(1, len(array)):
        pos = i-1
        aux = array[i]
        while pos >= 0 and aux < array[pos] :
                array[pos+1] = array[pos]
                pos -= 1
        array[pos+1] = aux


# Casos de prueba
test1 = [34,3,5,8,23,1]
test2 = [7,87,44,1,0,34,76]

insertionSort(test1)
insertionSort(test2)

print(test1)
print(test2)