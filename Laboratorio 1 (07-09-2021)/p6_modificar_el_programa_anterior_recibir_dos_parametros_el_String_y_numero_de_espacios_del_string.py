# Ejercicio 6
def frameSpace1(text, spaces): #Solución 1: varias variables
    # Modificar el programa anterior para definir el número de espacios entre el marco y las palabras. Es decir, la función ahora aceptará 2 parámetros, el número de espacios y el string (de una o más palabras)
    frameUpDown = ""
    frameMidle = ""
    frameFinal = ""
    for i in range(1,len(text)+5): #Frame de arriba y abajo
        frameUpDown += "*"
    frameUpDown += "\n"

    for i in range(1,len(text)+5): #Frame de medios
        if i == 1 or i == len(text)+4:
            frameMidle += "*"
        else: 
            frameMidle += " "
    frameMidle += "\n"

    # Frame completo
    frameFinal += frameUpDown
    for i in range(1,spaces+1):
        frameFinal += frameMidle
    frameFinal += f"* {text} * \n"
    for i in range(1, spaces):
        frameFinal += frameMidle
    frameFinal += frameUpDown
    return frameFinal
    

def frameSpace2(text, spaces): #Solución 2: una sola variable
    # Modificar el programa anterior para definir el número de espacios entre el marco y las palabras. Es decir, la función ahora aceptará 2 parámetros, el número de espacios y el string (de una o más palabras)
    frame = ""
    for i in range(1,len(text)+5): #Frame de arriba y abajo
        frame += "*"
    frame += "\n"

    for i in range(1,spaces+1):
        for i in range(1,len(text)+5): #Frame de medios
            if i == 1 or i == len(text)+4:
                frame += "*"
            else: 
                frame += " "
        frame += "\n"
    frame += f"* {text} * \n"
    for i in range(1,spaces+1):
        for i in range(1,len(text)+5): #Frame de medios
            if i == 1 or i == len(text)+4:
                frame += "*"
            else: 
                frame += " "
        frame += "\n"
    for i in range(1,len(text)+5): #Frame de arriba y abajo
        frame += "*"

    return frame

# Casos de prueba
test1 = frameSpace1("You only live once",3)
test2 = frameSpace2("Water fountain",3)
print(test1)
print(test2)