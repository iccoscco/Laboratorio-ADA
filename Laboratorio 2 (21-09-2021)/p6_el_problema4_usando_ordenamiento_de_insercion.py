import time
# Problema 6
# Hacer como el ejercicio 4, pero usando inserción
def generateList(size): 
    return list(range(size,0,-1))

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
init1 = time.perf_counter()
test1 = generateList(10)
insertionSort(test1)
end1 = time.perf_counter()
print(f"\nTiempo 1: {end1 - init1:0.6f}") 

init2 = time.perf_counter()
test2 = generateList(100)
insertionSort(test2)
end2 = time.perf_counter()
print(f"\nTiempo 2: {end2 - init2:0.6f}") 


init3 = time.perf_counter()
test3 = generateList(1000)
insertionSort(test3)
end3 = time.perf_counter()
print(f"\nTiempo 3: {end3 - init3:0.6f}") 

init4 = time.perf_counter()
test4 = generateList(10000)
insertionSort(test4)
end4 = time.perf_counter()
print(f"\nTiempo 4: {end4 - init4:0.6f}") 
