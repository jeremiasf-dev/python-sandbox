# toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0;
# si es par, evalúa un nuevo c0 como c0 ÷ 2;
# de lo contrario, si es impar, evalúe un nuevo  c0 como 3 × c0 + 1;
# si c0 ≠ 1, salta al punto 2.
# Nota: Aunque la consigna lo mencione, no pide precisamente que se verifique el número a ingresar, motivo
# por el cual no se verifica

c0 = int(input("Ingrese un número natural: \n >> "))
contador = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
        contador += 1
        print(c0)
    elif c0 % 2 == 1:
        c0 = 3 * c0 + 1
        contador += 1
        print(c0)
print("Pasos = " , contador)
