# Problema 5
import collections

# Un entrevistador escoge las personas que meno le toma entrevista, determinar cuanto demorara en llegar a entrevistarnos
def interview_wait(array):
    cola = collections.deque(array)
    value = 0
    first = 0
    last = len(cola) - 1
    while cola[first] != -1 and cola[last] != -1:
        if cola[first] < cola[last]:
            value  = value + cola[first]
            first = first + 1
        else:
            value  = value + cola[last]
            last = last - 1
    print(f"El tiempo que toma es: {value}")


test = [4,-1,5,2,3]
interview_wait(test)

