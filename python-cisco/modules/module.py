#!/usr/bin/env python3

# La línea que comienza con #! puede ser llamada como shebang.
# Para ss.oo Unix, indica al SO como ejecutar el contenido del archivo,
# en otras palabras, qué programa debe ejecutarse para interpretar el texto (en este caso python3)

""" module.py - un ejemplo sobre un módulo de python """
# La cadena superior colocada antes de las instrucciones, se denomina
# "doc-string" y debe explicar brevemente el prósito y el contenido del módulo..

__counter = 0 # El "__" antes de la variable counter se usa para "sugerir" que no se utilice, ya que python no posee encapsulación.

def suml(the_list): # Suma los elementos de una lista
	global __counter
	__counter += 1
	the_sum = 0
	for element in the_list:
		the_sum += element
	return the_sum

def prodl(the_list): # Multiplica los elementos de una lista
	global __counter
	__counter += 1
	prod = 1
	for element in the_list:
		prod *= element
	return prod

# Tanto suml() como prodl() están disponibles para ser importadas.


# Se utiliza la variable __name__ para detectar cuando se ejecuta el archivo de forma independiente.

if __name__ == "__main__":
	print("Prefiero ser un módulo, pero puedo hacer algunas pruebas para usted.")
	my_list = [i+1 for i in range(5)]
	print(suml(my_list) == 15)
	print(prodl(my_list) == 120)
