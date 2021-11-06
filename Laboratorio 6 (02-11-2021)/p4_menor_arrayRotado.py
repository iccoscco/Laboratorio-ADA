# Problema 4:
def menorElementBinary(array):
    # Encuentre el primer mayor o igual a x
    N = len(array)
    L = 0
    R = N - 1
    while L <= R:
        mid = L + (R - L) / 2
        mid = int(mid)

        if array[mid-1] < array[mid] :
            L = mid + 1
        else:
            R = mid - 1
    return array[L]
    # return array[mid-1]

# Casos de prueba
array1 = [5,6,8,10,12,14,16,2,3,4]
array2 = [5,6,8,10,12,2,3,4]
print(menorElementBinary(array1))
print(menorElementBinary(array2))