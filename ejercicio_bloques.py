# Python Essentials 1 - Ejercicio
# Se ingresa un número y este se piensa como una pirámide convencional formada por bloques
# El programa devuelve su altura

blocks = int(input("Ingresa el número de bloques: "))
aux = 0
height = 0
i = 0
while blocks != 0:
    aux += 1
    blocks -= aux
    i += 1
    height = i
    print(blocks)
    if (blocks - aux) < 0:
        i -= 1
        break
    elif blocks <= 0:
        break
print("La altura de la pirámide:", height)
