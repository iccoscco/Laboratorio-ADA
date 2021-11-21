# Problema 3
import collections
def caps_lock(cadena):
    # Cambiar la cadena de acuerdo a los caracteres de la misma
    # => $ -> bufer liberado  
    # => @ -> cambio de case
    cola = collections.deque([])
    entrada = 1
    for i in range(len(cadena)):
        if len(cadena) == 0:
            cola.append(cadena[i])
        else:
            if cadena[i] == "$":
                # Vaciar cola
                size = len(cola)
                for i in range(size):
                    print(cola.popleft(),end=" ")
                        
            else: 
                # Cambio de case
                if cadena[i] == "@":
                    entrada = entrada + 1

                # Inserción de datos
                if entrada % 2 != 0:
                    for k in range(len(cola)):
                        cola[k] = cola[k].lower()                    
                    cola.append(cadena[i].lower())
                else:
                    for m in range(len(cola)):
                        cola[m] = cola[m].upper()
                    cola.append(cadena[i].upper())
        
        # Eliminación de arroba
        if cadena[i] == "@":
            cola.popleft()    
                
                    
            

# Casos de prueba
caps_lock("abc$d@ef$@g$")