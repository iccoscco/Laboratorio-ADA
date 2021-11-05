# Problema 3:
def mayorIgualtBinary(array,number):
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
