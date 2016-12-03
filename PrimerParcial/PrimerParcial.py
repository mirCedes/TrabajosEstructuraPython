# -*- coding: utf-8 -*-
productos={
        0:{'Dulces':[0.05,"bolsa",30]},
        1:{'Pan':[0.15,"unidad",50]},
        2:{'Leche':[2.50,"galon",10]},
        3:{'Queso':[3.0,"libra",10]},
        4:{'Frijol':[0.78,"libra",200]},
        5:{'Arroz':[0.40,"libra",100]},
        6:{'Cereal':[3.40,"caja",100]},
        7:{'Jabon':[0.80,"unidad",30]},
        8:{'Embutidos':[1.20,"libra",55]},
        9:{'Jabon':[0.80,"unidad",10]},
        10:{'Arroz':[4.50,"libra",200]},
        }
def buscar():
    valor=raw_input("Buscar:")
    for k1 in productos.keys():
        for k, v in productos[k1].iteritems():
            if k== valor:
                print k
                print "Precio: ",v[0]
                print "Peso: ",v[1]
                print "Existencias: ",v[2]
def addProductoPrecio():
    nomMod=raw_input("¿Producto que se desea modificar? ")
    for k1 in productos.keys():
       for k, v in productos[k1].iteritems():
           e=0
           e2=0
           lista=[]
           lista.append(k)
           if k==nomMod:
               precio=raw_input("¿Precio del producto? ")
               existencia=int(raw_input("¿Existencias del producto? "))
               v[0]=precio
               e=v[2]
               e2=e+existencia
               v[2]=e2
               print "Nombre del producto: ",nomMod
               print "precio del producto: ",v[0]
               print "cantidad en existencias: ",v[2]
           if nomMod not in lista:
               print "Ingrese producto desde codigo"
                       

def modificar():
    for k1 in productos.keys():
       for k, v in productos[k1].iteritems():
            print "Id Producto: -",k1,"-Producto: ",k,"---Precio: ",v[0],"---Peso: ",v[1],"---Existencias: ",v[2]
        
def modificar2():
    valorModif=raw_input("¿Producto que se desea modificar? ")
    for k1 in productos.keys():
       for k, v in productos[k1].iteritems():
           lista=[]
           lista.append(k)
               
           if k==valorModif:
               precio=raw_input("¿Precio del producto a modificar? ")
               existencia=raw_input("¿Existencias del producto a modificar? ")
               v[0]=precio
               v[2]=existencia
               print "Nombre del producto: ",valorModif
               print "Nuevo precio del producto: ",v[0]
               print "Nueva cantidad en existencias: ",v[2]       
def vender():
    ex=0
    proVender=raw_input("¿producto que desea vender? ")
    for k1 in productos.keys():
       for k, v in productos[k1].iteritems():
           lista=[]
           lista.append(k)
           c=v[2]
           if k==proVender:
               cant=int(raw_input("¿Cantidad que desea vender? "))
               if c ==0:
                    print "No hay existencias"
               elif cant > c:
                   print "Ingrese una cantidad no muy alta de ", c
               else:
                    ex=v[2]-cant
                    v[2]=ex
def eliminar():
    valorEliminar=raw_input("¿Producto que se desea eliminar? ")
    for k1 in productos.keys():
        for k, v in productos[k1].iteritems():
            if k== valorEliminar:
                productos.pop(k1)
    print "El producto ",valorEliminar,"ha sido eliminado con exito"
def eliminarRepetidos():
    lista=[]
    for k1 in productos.keys():
        for k, v in productos[k1].iteritems():
            lista.append(k)
    precio=0.0
    cantidad=0
    indice=0
    indiceEliminar=0
    int(indice)
    DProductos=""
    for k1 in productos.keys():
        for k, v in productos[k1].iteritems():
            if lista.count(k)>1:
                if indice == 0:
                    indice=k1
                if indice > k1:
                    indice = k1
                if DProductos != k:
                    DProductos = k
                    if DProductos == DProductos:
                        cantidad=cantidad+ int(v[2])
                        precio=v[0]
                        indiceEliminar = k1
                    if indiceEliminar>indice:
                        productos[indice]={k: [precio,"unidad",cantidad]}
                        productos.pop(indiceEliminar)
                    precio=0.0
                    cantidad=0
                    indice=0
                    indiceEliminar=0
                    int(indice)
                    if indice == 0:
                        indice=k1
                    if indice > k1:
                        indice = k1
                    
                cantidad=cantidad+ int(v[2])
                precio=v[0]
                indiceEliminar = k1
                if indiceEliminar>indice:
                    productos[indice]={k: [precio,"unidad",cantidad]}
                    productos.pop(indiceEliminar)
while True:
        
        while True:
            print "1- Modificar producto"
            print "2- Eliminar producto"
            print "3- Buscar producto"
            print "4- Vender producto"
            print "5- Agregar Existencias y precios a productos"
        
            try:
                pregunta=int(raw_input("Ingrese un valor "))
            except:
                print "Ingrese un valor valido"
            if pregunta==1:
                eliminarRepetidos()
                modificar()
                modificar2()
            if pregunta==2:
                eliminar()
            if pregunta==3:
                buscar()
            if pregunta==4:
                eliminarRepetidos()
                modificar()
                vender()
            if pregunta==5:
                modificar()
                addProductoPrecio()
            