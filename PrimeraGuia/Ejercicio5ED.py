# -*- coding: utf-8 -*-
#Realice un script el cual cuente el número de veces que aparece ‘ana’ 
#en una cadena ejemplo: cadena=’adbananasddanadeeana’ en esta cadena si 
#se evaluá en el script tiene que mostrar como resultado ana aparece 4 veces en la cadena.
#Recuerde contar las palabras donde se encuentra ana una seguido de la otra o que la letra anterior la complementa ej. anana.
cadena='adbananasddanadeeana'
print len(cadena.split("ana"))