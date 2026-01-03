# !! Nota: No funciona como quiero porque es necesario utilizar funciones. Hago commit de todas formas.

# Me propongo a realizar un checklist de tareas (aún sin persistencia) utilizando listas.

# Variable para verificar si lo ingresado es la opción de salida (-1)
ingreso = ""

# Varibles para: 1) Ingresar la tarea. 2) Verificar el estado (False: Incompleta, True: Completa)
# Estas variables serán luego pasadas a una lista dentro de la lista.

tarea = ""
estado = False

# Lista dinámica
lista_tareas = []

while ingreso != "*":

    print("Gestor de tareas.")
    print("Menú de opciones.")
    print(" 1) Agregar tarea.")
    print(" 2) Mostrar tareas.")
    print(" *) Salir.")
    print(">> " , end="")

    ingreso = input()
    if ingreso == "*":
        break
    elif ingreso == "1":
        while ingreso != "*":
            print("Ingrese la tarea o presione '*' para salir.")
            ingreso = input(">> ")
            
            if ingreso == "*":
                break
            else:
                tarea = ingreso
                estado = False
                lista_tareas.append([tarea, estado])
    elif ingreso == "2":
        for i in lista_tareas:
            print(lista_tareas[i])
    else:
        print("Ingreso inválido, por favor, ingrese una opción válida.")