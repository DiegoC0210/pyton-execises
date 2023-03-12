cant10 = 5
cant20 = 5
cant50 = 5
cant100 = 5
#---------------Valor total de billetes -------------------
total10= cant10*10000
total20= cant20*20000
total50= cant50*50000
total100=cant100*100000

total= total10 + total20 + total50 + total100
Repetir = 0 
continuar = 0
#--------------------------------------------------------------- 

while total >=10000:
    cantRetiro= int(input("¿Cuanto deseas retirar?: "))
    
    Retirar = 0                                 #<--+
    CopyCantRetiro = cantRetiro                 #   |
    cantde100retirados = 0                      #   |----> Receteo de datos
    cantde50retirados = 0                       #   |
    cantde20retirados = 0                       #   |
    cantde10retirados = 0                       #<--+
    ccant10 = cant10
    ccant20 = cant20
    ccant50 = cant50
    ccant100 = cant100




#..........................CICLO QUE DA Y RESTA LOS BILLETES....................................      
    while CopyCantRetiro >= 100000 and ccant100 > 0 : # Compara si la cantidad que el usuario va a retirar es mayor o igual a la cantidad 
        Retirar = Retirar + 100000                    # del billete mas grande y si hay billetes de este valor disponibles
        cantde100retirados = cantde100retirados + 1   
        ccant100 = ccant100 - 1                         # y si sì, entonces se resta 1 billete a la cantidad disponible y se suma 1 billete
        CopyCantRetiro = CopyCantRetiro - 100000      # al dinero que va a retirar finalmente
           
        pass

    while CopyCantRetiro >= 50000 and ccant50 > 0 :
        Retirar = Retirar + 50000
        cantde50retirados = cantde50retirados + 1
        ccant50 = ccant50 - 1
        CopyCantRetiro = CopyCantRetiro - 50000
        pass

    while CopyCantRetiro >= 20000 and ccant20 > 0 :
        Retirar = Retirar + 20000
        cantde20retirados = cantde20retirados + 1
        ccant20 = ccant20 - 1
        CopyCantRetiro = CopyCantRetiro - 20000
        pass

    while CopyCantRetiro >= 10000 and ccant10 > 0 :
        Retirar = Retirar + 10000
        cantde10retirados = cantde10retirados + 1
        ccant10 = ccant10 - 1
        CopyCantRetiro = CopyCantRetiro - 10000
        pass
    if Retirar == cantRetiro :
        print("....................................................")
        print("Se pidio: ",Retirar)
        print("Se retiro: ",cantRetiro)
        print("---------------")
        print("Cantidad de billetes de 100.000: ",cantde100retirados)
        print("Cantidad de billetes de 50.000: ",cantde50retirados)
        print("Cantidad de billetes de 20.000: ",cantde20retirados)
        print("Cantidad de billetes de 10.000: ",cantde10retirados)
        print ("SE HA RETIRADO CORRECTAMENTE")
        print(".....................................................")
         
        cancelar=  int(input("si quieres cancelar la transaccion escribe 1, si quieres repetir escribe 2: "))
        if cancelar == 1:
            print("Haz cancelado la transaccion")
        else:
            cant10 = ccant10 
            cant20 = ccant20 
            cant50 = ccant50 
            cant100 = ccant100 
            CantRetiro = CopyCantRetiro
            
            total = total - Retirar
            print(total)
print("----------No hay billetes------------------")
pass