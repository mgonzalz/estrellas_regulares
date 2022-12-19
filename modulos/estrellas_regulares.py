from turtle import *
def estrella_regular(lados):
    color('black', 'black') # color de la estrella
    speed(4) # velocidad de la tortuga
    begin_fill() # comienza a rellenar
    for i in range(lados):
        forward(200) # avanza 200 pasos
        left(180-180/lados) # gira 180 - 180 / lados grados

    end_fill()
    done()
def inicio():
    print("Esto es una estrella regular")
    try: # comprobar si es un numero
        lados = int(input("¿Cuántos lados desea que tenga la estrella?: "))
        estrella_regular(lados)
    except ValueError:
        print("Debe ingresar un número")
        inicio()
