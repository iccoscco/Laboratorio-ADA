import time
# Problema 4
# Generar arreglos invertidos de 10, 100, 1000, 10 000, etc y hallar el tiempo de ejecución de cada uno. Hacer gráfica
def generateList(size): 
    return list(range(size,0,-1))

# Casos de prueba
init1 = time.perf_counter()
test1 = generateList(10)
end1 = time.perf_counter()

init2 = time.perf_counter()
test2 = generateList(100)
end2 = time.perf_counter()

init3 = time.perf_counter()
test3 = generateList(1000)
end3 = time.perf_counter()

init4 = time.perf_counter()
test4 = generateList(10000)
end4 = time.perf_counter()

init5 = time.perf_counter()
test5 = generateList(100000)
end5 = time.perf_counter()

print(f"\nTiempo 1: {end1 - init1:0.6f}") 
print(f"\nTiempo 2: {end2 - init2:0.6f}") 
print(f"\nTiempo 3: {end3 - init3:0.6f}") 
print(f"\nTiempo 4: {end4 - init4:0.6f}") 
print(f"\nTiempo 5: {end5 - init5:0.6f}") 