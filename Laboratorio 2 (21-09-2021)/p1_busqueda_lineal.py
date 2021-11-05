# Problema 1
array = [1,4,8,9,11,15,7,12,13,6]
element1 = 1
element2 = 34

# Realizar una búsqueda lineal
def search(array,element):
    for i in range(0,len(array)):
        if array[i] == element:
            return True
    return False

# Casos de prueba
print(search(array,element1))
print(search(array,element2))