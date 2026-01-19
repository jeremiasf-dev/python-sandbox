# El siguiente programa es muy simple, toma el primer elemento de la lista y lo compara con el resto de los elementos...
# Si encuentra un repetido, lo elimina, así de simple.

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

actual = 0

for i in my_list:

    actual = my_list[i]

    if actual == my_list[i]:

        del my_list[i]

print("La lista con elementos únicos:")

print(my_list)
