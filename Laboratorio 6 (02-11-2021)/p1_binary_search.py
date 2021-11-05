# Problema 1:

def binarySearch(array,target):
    # Binary Search sin overflow
    N = len(array)
    L = 0
    R = N - 1
    while L <= R:
        mid = L + (R - L) / 2
        mid = int(mid)
        if array[mid] == target:
            return mid
        if array[mid] < target:
            L = mid + 1
        else:
            R = mid - 1
    return -1

# Caso de prueba
array = [2,4,6,8,10,12]
print(binarySearch(array,17))