from os import system

system('cls')

estudiantes = {} # diccionario para almacenar estudiantes y sus calificaciones

def add_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    calificacion = float(input("Ingrese la calificación del estudiante: "))
    estudiantes[nombre] = calificacion
    print("El estudiante", nombre, "ha sido agregado con éxito.")

def mostrar_estudiantes():
    print("Lista de estudiantes con sus calificaciones:")
    for nombre, calificacion in estudiantes.items():
        print(nombre, ":", calificacion)

def calcular_promedio():
    calificaciones = estudiantes.values()
    promedio = sum(calificaciones) / len(calificaciones)
    print("El promedio de las calificaciones es:", promedio)

def calcular_aprobados():
    aprobados = sum(1 for calificacion in estudiantes.values() if calificacion >= 6)
    print("El número de aprobados es:", aprobados)

def mostrar_mejores_calificaciones():
    mejores_calificaciones = [nombre for nombre, calificacion in estudiantes.items() if calificacion == max(estudiantes.values())]
    print("Los estudiantes con la mejor calificación son:", ", ".join(mejores_calificaciones))
 
def mostrar_calificaciones_superiores_a_promedio():
    calificaciones = estudiantes.values()
    promedio = sum(calificaciones) / len(calificaciones)
    superiores_a_promedio = [nombre for nombre, calificacion in estudiantes.items() if calificacion > promedio]
    print("Los estudiantes con calificación superior al promedio son:", ", ".join(superiores_a_promedio))

def consultar_calificacion():
    nombre = input("Ingrese el nombre del estudiante a consultar: ")
    if nombre in estudiantes:
        calificacion = estudiantes[nombre]
        print("La calificación de", nombre, "es:", calificacion)
    else:
        print("El estudiante", nombre, "no se encuentra en la lista.")

def finalizar_programa():
    print("¡Gracias por utilizar el programa!")
    exit()
    

while True:
    print("BIENVENIDO AL PROGRAMA DE GESTION DE CALIFICACIONES")
    print('==='*20)
    print("[1] - Añadir estudiante y calificación")
    print("[2] - Mostrar lista de estudiantes con sus calificaciones")
    print("[3] - Calcular la promedio de las calificaciones")
    print("[4] - Calcular el número de aprobados")
    print("[5] - Mostrar los estudiantes con mejor calificación")
    print("[6] - Mostrar los estudiantes con calificación superior al promedio")
    print("[7] - Consultar la nota de un estudiante determinado")
    print("[8] - FINALIZAR EJECUCION DEL PROGRAMA")
    print('==='*20)
    opcion = input("Ingrese el número de la opción que desea ejecutar: ")

    if opcion == "1":
        add_estudiante()
        input('Presione ENTER para continuar')
        system('cls')
    elif opcion == "2":
        mostrar_estudiantes()
        input('Presione ENTER para continuar')
        system('cls')
    elif opcion == "3":
        calcular_promedio()
        input('Presione ENTER para continuar')
        system('cls')
    elif opcion == "4":
        calcular_aprobados()
        input('Presione ENTER para continuar')
        system('cls')
    elif opcion == "5":
        mostrar_mejores_calificaciones()
        input('Presione ENTER para continuar')
        system('cls')
    elif opcion == "6":
        mostrar_calificaciones_superiores_a_promedio()
        input('Presione ENTER para continuar')
        system('cls')
    elif opcion == "7":
        consultar_calificacion()
        input('Presione ENTER para continuar')
        system('cls')
    elif opcion == "8":
        finalizar_programa()
    else:
        system('cls')
        print("Opción inválida, por favor intente de nuevo.")