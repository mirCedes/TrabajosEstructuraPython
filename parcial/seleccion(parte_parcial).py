# -*- coding: utf-8 -*-
import csv
lis=[]
lis1=[]
lis2=[]
car=[]
car2=[]
li=[]
abrir=open('borrowers_test.csv')
ins=csv.reader(abrir,delimiter=',')
for line in ins:
	carrera=line[6].decode('utf8')
	car.append(carrera)
	car2=list(set(car))
	n=len(car2)
	for i in range(0,n-1):
		k=i
		t=car2[i]
		for j in range(i,n):
			if car2[j]<t:
				k=j
				t=car2[j]
		car2[k]=car2[i]
		car2[i]=t
for i in car2[:]:
	print i
