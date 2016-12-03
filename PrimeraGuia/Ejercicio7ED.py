# -*- coding: utf-8 -*-
#Cree un script el cual busque en una cadena el numero menor y el mayor, dichos número
#tiene que ser eliminados de la lista y generar el cubo de cada numero es decir que si el
#numero menor es 1 el cubo es 1, 3 es 9 este resultado de agregara al final de la lista.
#Numeros=[6,2,5,9,1,8,12,45,22,3]
numeros=[6,2,5,9,1,8,12,45,22,3]
mayor=max(numeros)
menor=min(numeros)
for i in numeros:
    if mayor==i:
        numeros.remove(i)
    elif menor==i:
        numeros.remove(i)
numeros.append(pow(menor,3))
numeros.append(pow(mayor,3))
print numeros