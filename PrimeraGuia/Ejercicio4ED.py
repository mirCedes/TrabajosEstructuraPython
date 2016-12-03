# -*- coding: utf-8 -*-
#Elabore un script el cual cuente el número de palabras que se encuentran en la siguiente
#Frase: se recomienda el uso de la función split() 
#frase=”La mayoría de los buenos programadores programan, 
#no porque esperan que se les pague o por adulación por parte del público, sino porque es divertido programar”.
frase="La mayoria de los buenos programadores programan, no porque esperan que se les pague o por adulacion por parte del publico, sino porque es divertido programar".split(" ")
contador=0
for x in range(len(frase)):
            contador +=1
print contador, " palabras"