# Problema 3:
def mayorIgualBinary(array,number):
    # Encuentre el primer mayor o igual a x
    N = len(array)
    L = 0
    R = N - 1
    aux = 0
    while L <= R:
        mid = L + (R - L) / 2
        mid = int(mid)
        if array[mid] == number:
            return array[mid]
        if array[mid] < number:
            L = mid + 1
        else:
            R = mid - 1
        aux = array[mid]

    return aux

# Casos de prueba
array = [2,3,5,6,8,10,12]
print(mayorIgualtBinary(array,7))
print(mayorIgualtBinary(array,11))