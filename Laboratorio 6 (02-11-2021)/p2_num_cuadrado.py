# Problema 2
def sqrtBinary(number):
    # Determinar si un número es cuadrado usando la búsqueda binaria
    N = number
    L = 0
    R = N - 1
    while L <= R:
        mid = L + (R - L) / 2
        mid = int(mid)
        if mid * mid == number:
            return mid
        if mid * mid < number:
            L = mid + 1
        else:
            R = mid - 1
    return -1

# Casos de prueba
print(sqrtBinary(64))
print(sqrtBinary(79))