
# 1. Convert from O(n^2) to O(n)
def greatestNumber(array):
    greatest = array[0]
    for i in range(len(array)):
        if array[i] > greatest:
            greatest = array[i]
    return greatest
    
            
            
        
# casos de prueba
array = [12,13,1,43,53]
print(greatestNumber(array))