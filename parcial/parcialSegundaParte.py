#!/usr/bin/python
# -*- coding: utf-8 -*
#vista de datos SELECT
import sqlite3
cnn = sqlite3.connect('datos_empleados.db')
sql1='''
 SELECT empleado.id, empleado.nombre,empleado.salario FROM empleado;
 '''
salario=[]
ide=[]
cursor1 = cnn.execute(sql1)
for row in cursor1:
	salario.append(row[2])
	
	
	if row[0] not in ide[:]:
		if row[2]>0.01 and row[2]<=472.00:
			ide.append(row[0])
			descEx=0
			descA=0
			salF=row[2]
			afp=row[2]*0.0625
			afp=round(afp,2)
			isss=row[2]*0.03
			isss=round(isss,2)
			salRetencion=row[2]-(afp+isss)
			salRetencion=round(salRetencion,2)
			cnn.execute("INSERT INTO pago_empleados (descuento_afp,descuento_isss,renta,salario_neto,id_empleado) VALUES(?,?,?,?,?)",(afp,isss,descA,salRetencion,row[0]))
			cnn.commit()
		if row[2]>472.00 and row[2]<=895.24:
			ide.append(row[0])
			descEx=row[2]-472.00
			descA=descEx*0.10
			TotalExceso=descA+17.67
			TotalExceso=round(TotalExceso,2)
			afp=row[2]*0.0625
			afp=round(afp,2)
			isss=row[2]*0.03
			isss=round(isss,2)
			salNeto=row[2]-(afp+isss+TotalExceso)
			salNeto=round(salNeto,2)
			cnn.execute("INSERT INTO pago_empleados (descuento_afp,descuento_isss,renta,salario_neto,id_empleado) VALUES(?,?,?,?,?)",(afp,isss,TotalExceso,salNeto,row[0]))
			cnn.commit()
		if row[2]>895.24 and row[2]<=2038.10:
			ide.append(row[0])
			renta=((row[2]-895.24)*0.20)+60.00
			renta=round(renta,2)
			afp=row[2]*0.0625
			afp=round(afp,2)
			isss=row[2]*0.03
			isss=round(isss,2)
			salNeto=row[2]-(afp+isss+renta)
			salNeto=round(salNeto,2)
			cnn.execute("INSERT INTO pago_empleados (descuento_afp,descuento_isss,renta,salario_neto,id_empleado) VALUES(?,?,?,?,?)",(afp,isss,renta,salNeto,row[0]))
			cnn.commit()
		if row[2]>2038.11:
			ide.append(row[0])
			descEx=row[2]-2038.10
			descA=descEx*0.30
			TotalExceso=descA+288.57
			TotalExceso=round(TotalExceso,2)
			afp=row[2]*0.0625
			afp=round(afp,2)
			isss=row[2]*0.03
			isss=round(isss,2)
			salNeto=row[2]-(afp+isss+TotalExceso)
			salNeto=round(salNeto,2)
			cnn.execute("INSERT INTO pago_empleados (descuento_afp,descuento_isss,renta,salario_neto,id_empleado) VALUES(?,?,?,?,?)",(afp,isss,TotalExceso,salNeto,row[0]))
			cnn.commit()
consulta='''select empleado.nombre,pago_empleados.descuento_afp,pago_empleados.descuento_isss,
pago_empleados.renta, pago_empleados.salario_neto  FROM empleado,pago_empleados 
where empleado.id=pago_empleados.id_empleado ORDER BY pago_empleados.salario_neto'''
cursor2 = cnn.execute(consulta)
for row in cursor2:
	print "Nombre: ",row[0]
	print "Descuento AFP: ",row[1]
	print "Descuento ISSS: ",row[2]
	print "Renta: ",row[3]
	print "Salario Neto: ",row[4]
	print "-----------------------------"
cnn.close()
