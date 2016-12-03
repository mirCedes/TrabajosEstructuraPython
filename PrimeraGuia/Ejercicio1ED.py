# -*- coding: utf-8 -*-
#Ejercicio numero 1
#Dado un rango de 20 números agregue a una lista los valores pares y en otra los impares:
#Use la instrucción if para validar y 2 listas para almacenar los mencionados números pares e impares.
desde=0
par=''
impar=''
while desde<= 19:
    if desde%2==0:
        par += ' %i' % desde
        pares=[par]
    desde += 1
    if desde%2>0:
        impar += ' %i' % desde
        impares=[impar]
    desde += 1
print 'Pares ',pares,' Impares ', impares