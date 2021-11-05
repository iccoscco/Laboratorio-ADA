# Problema 3
import time

# Del problema 2 hallar el tiempo de ejecución
def generateList(size):
    return list(range(size,0,-1))

def searchInvertArray(array, element):
    for i in range(0,len(array)):
        if array[i] == element:
            return True
    return False

# Casos de prueba
init = time.perf_counter()

test1 = generateList(18)
test2 = generateList(89)

print(searchInvertArray(test1,78))
print(searchInvertArray(test2,15))

end = time.perf_counter()

print(f"\nTiempo de ejecución {end - init:0.6f}") 
