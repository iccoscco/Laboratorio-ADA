# Problema 6
from heapq import merge

 
def merge_list(array):
# Unir las listas de lista usando heaps
    heap = []
    for i in range(len(array)):
        heap = list(merge(heap, array[i]))   

    print(heap)
    
    

# Casos de prueba
test = [[1,4,5],[1,3,4],[2,6]]
merge_list(test)