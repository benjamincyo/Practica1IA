#!/usr/bin/env python
import csv, sys,os,math,random
os.system('clear')
#tethasFinal=[1,2,1];
tethasFinal=[];
def menu():
	opcion=0;
	while (opcion!=2):
		print "*****Gradiente Descendente*****"
		print "1. Algoritmo Gradiente Descendente"
		print "2. Salir"
		opcion=input("Eliga una opcion: \n")
		if(opcion==1):
			os.system('clear');
			print "*****Algoritmo Gradiente Descendente*****";
			pathX=raw_input("Direccion archivo variableX.csv: ");
			pathY=raw_input("Direccion archivo variableY.csv: ");
			alfa=input("Parametro alfa: ");
			tolerancia=input("Tolerancia: ");
			iterraciones=input("Iteraciones: ");
			escribirCosto("costo.csv","********Costo**********","w")
			if(os.path.exists(pathX) and os.path.exists(pathY)):
				print "\n----------Salida Parametros Tethas----------\n"
				print GradienteDescendente(iterraciones,m(pathX),n(pathX),variableX(pathX),variableY(pathY),tethasFinal,alfa,tolerancia)
				print "\n----------Archivo de costos generado con exito----------"
			else:
				print "Error datos invalidos"
			menu()
		elif opcion == 2:
			sys.exit();
			
def n(varX):
	nX=0;
	if(os.path.exists(varX)):
		reader =csv.reader(open(varX,'rb'))
		for index,row in enumerate(reader):
			nX=len(row);
	else:
		print "Archivo no existe"			
	return nX-1;
	
def m(varX):
	l=[];
	if(os.path.exists(varX)):
		reader =csv.reader(open(varX,'rb'))
		for index,row in enumerate(reader):
			l.append(row)
	else:
		print "Archivo no existe"			
	return len(l)-1;
	
def variableX(archivoX):
	listaX=[];
	if(os.path.exists(archivoX)):
		reader = csv.reader(open(archivoX,'rb'))
		for index, row in enumerate(reader):
			listaX.append(row);
	else:
		print "Archivo no existe"
	return listaX;
	
def variableY(archivoY):
	listaY=[];
	if(os.path.exists(archivoY)):
		reader = csv.reader(open(archivoY,'rb'))
		for index, row in enumerate(reader):
			listaY.append(row);
	else:
		print "Archivo no existe"
	return listaY;

def derivada(m,n,varx,vary,tethas):
	r=0.0
	for i in range (0,m+1):
		r=r+(hxi(i,n,varx,vary,tethas)-yi(vary,i))*xi(varx,i,n);
	return r;
	
def hxi(m,n,variableX,variableY,tethas):
	x=variableX[m];
	y=variableY[m];
	h=0.0;
	for i in range(0,n+1):
		h=h+float(tethas[i])*float(x[i]);
	return float(h);	

def yi(variableY,m):
	y=variableY[m];
	return float(y[0]);
	
def xi(variableX,m,n):
	x=variableX[m];
	return float(x[n])
	
def GradienteDescendente(iteraciones,m,n,varx,vary,tethas,alfa,tolerancia):

	for j in range(0,n+1):
		tethasFinal.append(float(random.randint(1,3)));

	i=0;
	while (i<iteraciones and funcionCosto(m,n,varx,vary,tethasFinal)>tolerancia):
		for k in range (0,n+1):
			tethasFinal[k]=tethasFinal[k]-(alfa/m)*derivada(m,k,varx,vary,tethasFinal);
		i=i+1;		
	return tethasFinal;
			

def funcionCosto(m,n,varx,vary,tethas):
	constante=0.5 *m;
	r=0.0;
	for i in range (0,m+1):
		r=r+(hxi(i,n,varx,vary,tethas)-yi(vary,i));	
	r=r**2
	escribirCosto("costo.csv",str(r),"a")
	return float(constante*r);	
	
	
def escribirCosto(archivo,costo,tipo):
	f=open(archivo,tipo)
	f.write(costo)
	f.write("\n")
	f.close()
		
if __name__ == "__main__":
	menu()
		
