# *Problema 2
import math

# ***SOlUCIÓN


def searchMatriz(matrix, element):
    # * Implementar la búsqueda binaria, para buscar un elemento dentro de una matriz
    high = len(matrix) * len(matrix[0]) - 1
    low = 0
    middle = 0
    row = 0
    col = 0
    while low <= high:
        # Matriz cuadrada
        middle = int((high + low) / 2)

        # Índices
        dimension = len(matrix)
        row = math.floor(middle / dimension)
        col = middle % dimension

        # Búsqueda
        if matrix[row][col] == element:
            return f"Posición ({row+1},{col+1})"
        elif element > matrix[row][col]:
            low = middle + 1
        else:
            high = middle - 1

    return False


# ***Casos de prueba 2
test1 = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
print(searchMatriz(test1, 5))
print(searchMatriz(test1, 11))
print(searchMatriz(test1, 17))

test2 = [[2, 4, 6, 8], [10, 12, 14, 16], [18, 20, 22, 24], [26, 28, 30, 32]]
print(searchMatriz(test2, 6))
print(searchMatriz(test2, 22))
print(searchMatriz(test2, 32))
print(searchMatriz(test2, 9))
