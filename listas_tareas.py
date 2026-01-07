# Me propongo a realizar un checklist de tareas (aún sin persistencia) utilizando listas.
# Por hacer: Que funcione la función mostrar_tareas (Se queda en el loop y aún no permite la eliminación de tareas.) 
# Variables

# Lista dinámica
lista_tareas = []

# Funciones

#########################################################
def limpiar_pantalla():
    import os
    os.system("clear")
#########################################################

#########################################################
def agregar_tarea():
    salida = False
    while not salida:        
        limpiar_pantalla()
        print("Ingrese tarea o presione '*' para salir.")
        tarea = input(">> ")
        if tarea == "*":
            salida = True
        else:
            lista_tareas.append(tarea)
#########################################################


#########################################################
def mostrar_tareas():
    
    contador = 0
    salida = False

    while not salida:    
        limpiar_pantalla()

        print("Lista de tareas: ")

        for tarea in lista_tareas:
            contador += 1
            print(contador, ") ", tarea)

        print("Seleccione una opción:")
        print("1) Eliminar tarea.")
        print("*) Volver al menú.")
        print(">> " , end="")

        ingreso = input
        if ingreso == "1":
            print("WIP")
        elif ingreso == "*":
            salida = True
        else:
            print("Opción inválida.")
#########################################################


#########################################################
def menu_opciones():
    limpiar_pantalla()
    print("Gestor de tareas.")
    print("Menú de opciones.")
    print(" 1) Agregar tarea.")
    print(" 2) Mostrar tareas.")
    print(" *) Salir.")
    print(">> " , end="")

    ingreso = input()
    if ingreso == "*":
        return True
    elif ingreso == "1":
        agregar_tarea()
    elif ingreso == "2":
        #mostrar_tareas()
        print("WIP")
    else:
        print("Error. Ingrese una opción válida.")

    return False
#########################################################


# Comienzo del programa

# Inicialización de variables
salida = False

# Cuerpo del programa

while not salida:
    salida = menu_opciones()