#Juego de numeros al azar de numeros Randoms
import os
import random
num=random.randint(1,100)
#El numero de intentos -contador
contador=0
name=True
os.system("cls")
while name:
    
    num_1=(int(input("Digite el numero del 1 al 100 que vas a adivinar")))
    if num_1 <num:
        print("El numero es mayor")
        contador=contador+1
        pass
    
    elif num_1 > num:
         print("El numero es menor")
         contador=contador+1
         pass
    
    elif num_1 == num:
        contador=contador+1
        print("Has logrado adivinar el numero al azar")
        print("Tu cantidad de intentos son :", contador )
        input("Presione ENTER para continuar....")
        os.system ("cls")
        opcion=int(input("¿Quieres volver a jugar?\nsi=1 \nno=2\n:"))    
        if opcion == 2:
            name = False
        else:
            os.system("cls")
            num=random.randint(1,100)
            contador = 0
print("Te esperamos nuevamente")