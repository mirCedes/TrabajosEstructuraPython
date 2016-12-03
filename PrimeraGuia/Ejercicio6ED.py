# -*- coding: utf-8 -*-
#Cree un script el cual dada una lista busque los valores repetido y si los encuentra crea
#una nueva lista la cual contendrá los valores repetidos de la lista uno y para finalizar muestra
#la lista 1 ordenada de menor a mayor y la lista 2 de mayor a menor.
#Lista1=[1,3,4,5,7,8,9,2,5,6,4,12,20,3,7,9,0,1,4,3,8]
lista1=[1,3,4,5,7,8,9,2,5,6,4,12,20,3,7,9,0,1,4,3,8]
repetidos=[]
unicos=[]
for i in lista1:
    if i not in unicos:
        unicos.append(i)
    elif i not in repetidos:
        repetidos.append(i)
lista1.sort()
repetidos.sort(reverse=True)
print lista1
print repetidos