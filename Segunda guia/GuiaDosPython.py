# -*- coding: utf-8 -*-
import os
import sys
import webbrowser
import subprocess
from subprocess import Popen

def NuevoDirectorio():
	nombreDirectorio=raw_input("Ingrese nombre del nuevo directorio:")
	if os.path.exists(nombreDirectorio):
		print "---------------------AVISO--------------------------"
		print "El nombre de directorio ingresado ya existe!!!"
		print "Favor ingrese un nombre diferente"
		print "----------------------------------------------------"
	else:
		os.mkdir(nombreDirectorio,0777 )
		print "---------------------.........----------------------"
		print "Directorio creado con exito"
		print "----------------------------------------------------"
def DescargaSitio():
	enlace=raw_input("Ingrese url del sitio a descargar:")
	if os.path.exists(HTML):
		archivo=subprocess.Popen(['wget', '-Q1024m', '-i', '--no-parent', enlace], stdout=subprocess.PIPE)
	else:
		print "---------------------AVISO--------------------------"
		print "Favor cree un directorio HTML"
		print "----------------------------------------------------"
def DescargaImg():
	enlace=raw_input("Ingrese url de imagen a descargar:")
	if os.path.exists(IMG):
		archivo=subprocess.Popen(['wget', '-Q1024m', '-i', '--no-parent', enlace], stdout=subprocess.PIPE)
	else:
		print "---------------------AVISO--------------------------"
		print "Favor cree un directorio IMG"
		print "----------------------------------------------------"
def BuscarArchivos():
	nombreDirectorio=raw_input("Ingrese nombre del directorio:")
	if os.path.exists(HTML):
		nombreArchivo=nombreDirectorio+".html"
		os.system("cd HTML/")
		if os.path.exists(nombreArchivo):
			navegador=webbrowser("Firefox")
			webbrowser.open_new(nombreArchivo)
		else:
			print "El nombre del archivo ingresado no existe!!!"
	else:
		print "---------------------AVISO--------------------------"
		print "El nombre de directorio ingresado no existe!!!"
		print "Favor cree un archivo HTML"
		print "----------------------------------------------------"
def Capacidad():
	os.system("ls -h -l")		
def Salir():
	sys.exit()	
while True:   
        while True:
            print "1) Crear directorio de trabajo"
            print "2) Descargar sitio html"
            print "3) Descargar archivos con extensión de imágenes"
            print "4) Buscar archivos html"
            print "5) Mostrar la capacidad en Mega bite"
            print "6) Salir"
        
            try:
                pregunta=int(raw_input("Ingrese un valor: "))
            except:
                print "Ingrese un valor valido"
            if pregunta==1:
                NuevoDirectorio()
            if pregunta==2:
				DescargaSitio()
            if pregunta==3:
                DescargaImg()
            if pregunta==4:
				BuscarArchivos()
            if pregunta==5:
				Capacidad()
            if pregunta==6:
                Salir()
            
