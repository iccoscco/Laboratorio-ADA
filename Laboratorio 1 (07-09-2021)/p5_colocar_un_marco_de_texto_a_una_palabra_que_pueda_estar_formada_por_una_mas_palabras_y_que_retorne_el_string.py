# Ejercicio 5
def frameString1(text): #Solución 1: Varias variables
    # Colocar un marco a un texto. Escribir una función que reciba como parámetros un string (que puede estar formado por una o más palabras) y retorne otro string con las palabras colocadas en un marco
    frameUpDown = ""
    for i in range(1,len(text)+5):
        frameUpDown += "*"
    frameMidle = ""
    for i in range(1,len(text)+5):
        if i == 1 or i == len(text)+4:
            frameMidle += "*"
        else: 
            frameMidle += " "
    word = f"* {text} * "
    return f"{frameUpDown}\n{frameMidle}\n{word}\n{frameMidle}\n{frameUpDown}"

def frameString2(text): #Solución 2: Una variables
    frame = ""
    for i in range(1,len(text)+5):
        frame += "*"
    frame += "\n"

    for i in range(1,len(text)+5):
        if i == 1 or i == len(text)+4:
            frame += "*"
        else: 
            frame += " "
    frame += "\n"
    frame += f"* {text} * \n"
    
    for i in range(1,len(text)+5):
        if i == 1 or i == len(text)+4:
            frame += "*"
        else: 
            frame += " "
    frame += "\n"
    
    for i in range(1,len(text)+5):
        frame += "*"
    return frame

# Casos de prueba
test1 = frameString1("Never, never give up!")
test2 = frameString2("The Asterik War!!")
print(test1)
print(test2)
    