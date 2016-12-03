# -*- coding: utf-8 -*-
import csv
import numpy as np
import matplotlib.pyplot as plt

def votantesRepetidos():
	abrirArchivo = open('encuesta_espanol.txt')
	ins = csv.reader(abrirArchivo,delimiter='-')	
	print "#La siguiente es una lista de los que votaron más de una ves"
	
	ListaNombres = []
	for line in ins:
		ListaNombres.append(line[0].strip())
	nombresNoRepetidos = list(set(ListaNombres))
	
	for name in nombresNoRepetidos[:]:
		if ListaNombres.count(name) > 1:
			print name," voto ", ListaNombres.count(name), " veces."
	print "#==========================================================#"		
	
def CoteoDeVotos(vegetal):
	abrirArchivo = open('encuesta_espanol.txt')
	ins = csv.reader(abrirArchivo,delimiter='-')	
	count = 0
	for line in ins:
		gusto = line[1].strip()
		if gusto in vegetal:
			count = count +1
	return count
	
def FrutasConSusVotos(vegetal):
	abrirArchivo = open('encuesta_espanol.txt')
	ins = csv.reader(abrirArchivo,delimiter='-')	
	print("El numero de botos para " + vegetal + ".........")
	count = 0
	for line in ins:
		gusto = line[1].strip()
		if gusto in vegetal:
			count = count +1
	return count
	print "#==========================================================#"

def graficaCircular():
	Frutas = ["Pepinos","Kiwi","Rabano","Aguacate","Fresas","Tomates","Frijoles","Lechuga","Sandia","Papas","Brocoli"]
	ValoresGrafico = (CoteoDeVotos("Pepinos"), CoteoDeVotos("Kiwi"), CoteoDeVotos("Rabano"), CoteoDeVotos("Fresas"), CoteoDeVotos("Aguacate"), CoteoDeVotos("Tomates"), CoteoDeVotos("Frijoles"), CoteoDeVotos("Lechuga"), CoteoDeVotos("Sandia"), CoteoDeVotos("Papas"), CoteoDeVotos("Brocoli"))
	colors = ['c', 'w', 'r', 'y', 'g', 'b', 'm', 'lightskyblue', 'gray', 'orange','gold']
	plt.pie(ValoresGrafico, labels = Frutas, colors=colors, autopct = '%2.1f%%', shadow = True, startangle = 90)
	fig = plt.figure()
	ax = fig.gca()
	plt.show()
	
while True:
	print "Welcome"
	print "1- Ver resultados por fruta."
	print "2- Ver primer lugar."
	print "3- Ver los que votaron mas de una vez"
	print "4- Ver grafica de datos"
	
	while True:
		try:
			opcion = int(raw_input("Ingrese una opcion: "))
			break
		except:
			print "Ingrese una aopcion valida"
	if opcion == 1:
		print "Seleccione un literal para motrar su resultado"
		print '1- Brocoli'
		print '2- Lechuga'
		print '3- Fresas'
		print '4- Rabano'
		print '5- Kiwi'
		print '6- Frijoles'
		print '7- Tomates'
		print '8- Papas'
		print '9- Pepinos'
		print '10- Aguacate'
		print '11- Sandia'
		while True:
			try:
				itemEscoger = int(raw_input("Seleccione un item "))
				break
			except:
				print "Ingrese una opcion valida"
		if itemEscoger == 1:
			print FrutasConSusVotos("Brocoli")
		elif itemEscoger == 2:
			print FrutasConSusVotos("Lechuga")
		elif itemEscoger == 3:
			print FrutasConSusVotos("Fresas")
		elif itemEscoger == 4:
			print FrutasConSusVotos("Rabano")
		elif itemEscoger == 5:
			print FrutasConSusVotos("Kiwi")
		elif itemEscoger == 6:
			print FrutasConSusVotos("Frijoles")
		elif itemEscoger == 7:
			print FrutasConSusVotos("Tomates")
		elif itemEscoger == 8:
			print FrutasConSusVotos("Papas")
		elif itemEscoger == 9:
			print FrutasConSusVotos("Pepinos")
		elif itemEscoger == 10:
			print FrutasConSusVotos("Aguacate")
		elif itemEscoger == 11:
			print FrutasConSusVotos("Sandia")
		print "#==========================================================#"
	if opcion == 2:
		print "primer lugar"
		Frutas = ["Pepinos","Kiwi","Rabano","Aguacate","Fresas","Tomates","Frijoles","Lechuga","Sandia","Papas","Brocoli"]
		votosPrimerLugar = 0
		nombrePrimerLugar = ""
		
		for fru in Frutas[:]:
			aspiraPrimero = 0
			int(aspiraPrimero)
			aspiraPrimero = CoteoDeVotos(fru)
			if votosPrimerLugar < aspiraPrimero:
				votosPrimerLugar = aspiraPrimero
				nombrePrimerLugar = fru
		print nombrePrimerLugar, " con una cantidad de ", votosPrimerLugar, " votos"
		print "#==========================================================#"
	if opcion == 3:
		votantesRepetidos()
	if opcion == 4:
		graficaCircular()
