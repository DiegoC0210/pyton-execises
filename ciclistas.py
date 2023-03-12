import os


def operacion (Jugador):
    total = 0
    for i in range (0,5):
        total= total + Jugador[i]

    return(total)

os.system("cls")

ciclistas = ["Juan","Diego","Daniel","Alberto","Cumaco"]

puntajes = [[14600,24350,12940,35422,16345],
            [24350,14500,17450,31200,23501],
            [24350,14500,17450,31200,23501],
            [14320,24350,24350,23501,14320],
            [31200,23501,24350,12940,14320]]


#------------Ganador de la CARRERA-------------------------------------


resultado = []
for F in range (5):
    Suma = 0
    for C in range (5):
        Suma = Suma + puntajes[F][C]

    resultado.append(Suma)
    
#print(resultado)

ganador = min(resultado)

hola = 4
for i in range(hola):
    if resultado[i] == ganador:
        print(ciclistas[i]," Es el ganador de la CARRERA :,) \n con el puntaje de: ",ganador)
        hola = i


#-------------------------------------------------------------------------

input("Enter...")

resultado = []
suma = 0
for C in range (5):
    for F in range(5):
        resultado.append(puntajes[F][C])

        
    ganador = min(resultado)

    hola = 5
    for i in range(hola):
        if resultado[i] == ganador:
            print("Etapa : ",C)
            print("Ciclista: ",ciclistas[i])
            print("Tiempo: ",ganador)
            print("--------------------------------")
            hola = i


    resultado = []

