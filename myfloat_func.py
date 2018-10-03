#!/usr/bin/python
# -*- coding: utf8 -*-

def imprimir(a):
	entero="".join(str(e) for d in c[0])
	decimal="".join(str(e) for d in c[1])
	numero=entero+','+decimal
	return numero

def suma (a,b):
	a[0].reverse()
	b[0].reverse()
	e1="".join(str(e) for e in a[0])
	e2="".join(str(e) for e in b[0])
	d1="".join(str(e) for e in a[1])
	d2="".join(str(e) for e in b[1])
	if a[0][0]=="-":
		e1=int(e1.replace('-',""))
		d1=float('0.'+d1)
		e1=e1*-1
		d1=d1*-1
	else:
		e1=float(e1.replace("+",""))
		d1=float('0.'+d1)
	if b[0][0]=='-': 
		e2=float(e2.replace('-',""))
		d2=float("0."+d2)
		e2=e2*-1
		d2=d2*-1
	else:
		e2=float(e2.replace('+',""))
		d2=float("0."+d2)
		
	a[0].reverse()
	b[0].reverse()
	n1=e1+d1
	n2=e2+d2
	res=n1+n2
	res= float(res)
	
	if res>0:
		er=int(res)
		dr=res-int(res)
		e="+"+str(er)
		d=str(dr)
		e=list(e)
		d=list(d)
		d.pop(0)
		d.pop(0)
	else:
		er= int(res)
		dr=res+int(res)
		e="-"+str(er)
		d=str(dr)
		e=list(e)
		d=list(d)
	c=(e,d)
	return c 
	
	
    pass


def resta(a, b):
	a[0].reverse()
	b[0].reverse()
	e1="".join(str(e) for e in a[0])
	e2="".join(str(e) for e in b[0])
	d1="".join(str(e) for e in a[1])
	d2="".join(str(e) for e in b[1])
	if a[0][0]=="-":
		e1=int(e1.replace('-',""))
		d1=float('0.'+d1)
		e1=e1*-1
		d1=d1*-1
	else:
		e1=float(e1.replace("+",""))
		d1=float('0.'+d1)
	if b[0][0]=='-': 
		e2=float(e2.replace('-',""))
		d2=float("0."+d2)
		e2=e2*-1
		d2=d2*-1
	else:
		e2=float(e2.replace('+',""))
		d2=float("0."+d2)
		
	a[0].reverse()
	b[0].reverse()
	n1=e1+d1
	n2=e2+d2
	res=n1-n2
	res= float(res)
	print (res)
	if res>0:
		er=int(res)
		dr=res-int(res)
		e="+"+str(er)
		d=str(dr)
		e=list(e)
		d=list(d)
		d.pop(0)
		d.pop(0)
	else:
		er= int(res)
		dr=res+int(res)
		e="-"+str(er)
		d=str(dr)
		e=list(e)
		d=list(d)
		d.pop(0)
		d.pop(0)
	c=(e,d)
	return c
    pass


def multiplicacion(a, b):
	a[0].reverse()
	b[0].reverse()
	e1="".join(str(e) for e in a[0])
	e2="".join(str(e) for e in b[0])
	d1="".join(str(e) for e in a[1])
	d2="".join(str(e) for e in b[1])
	if a[0][0]=="-":
		e1=int(e1.replace('-',""))
		d1=float('0.'+d1)
		e1=e1*-1
		d1=d1*-1
	else:
		e1=float(e1.replace("+",""))
		d1=float('0.'+d1)
	if b[0][0]=='-': 
		e2=float(e2.replace('-',""))
		d2=float("0."+d2)
		e2=e2*-1
		d2=d2*-1
	else:
		e2=float(e2.replace('+',""))
		d2=float("0."+d2)
		
	a[0].reverse()
	b[0].reverse()
	n1=e1+d1
	n2=e2+d2
	res=n1*n2
	res= float(res)
	print (res)
	if res>0:
		er=int(res)
		dr=res-int(res)
		e="+"+str(er)
		d=str(dr)
		e=list(e)
		d=list(d)
		d.pop(0)
		d.pop(0)
	else:
		er= int(res)
		dr=res+int(res)
		e="-"+str(er)
		d=str(dr)
		e=list(e)
		d=list(d)
		d.pop(0)
		d.pop(0)
	c=(e,d)
	return c
    pass


def division(a, b):
	a[0].reverse()
	b[0].reverse()
	e1="".join(str(e) for e in a[0])
	e2="".join(str(e) for e in b[0])
	d1="".join(str(e) for e in a[1])
	d2="".join(str(e) for e in b[1])
	if a[0][0]=="-":
		e1=int(e1.replace('-',""))
		d1=float('0.'+d1)
		e1=e1*-1
		d1=d1*-1
	else:
		e1=float(e1.replace("+",""))
		d1=float('0.'+d1)
	if b[0][0]=='-': 
		e2=float(e2.replace('-',""))
		d2=float("0."+d2)
		e2=e2*-1
		d2=d2*-1
	else:
		e2=float(e2.replace('+',""))
		d2=float("0."+d2)
		
	a[0].reverse()
	b[0].reverse()
	n1=e1+d1
	n2=e2+d2
	res=n1/n2
	res= float(res)
	print (res)
	if res>0:
		er=int(res)
		dr=res-int(res)
		e="+"+str(er)
		d=str(dr)
		e=list(e)
		d=list(d)
		d.pop(0)
		d.pop(0)
	else:
		er= int(res)
		dr=res+int(res)
		e="-"+str(er)
		d=str(dr)
		e=list(e)
		d=list(d)
		d.pop(0)
		d.pop(0)
	c=(e,d)
	return c 
    pass


def comparacion(a, b):
	a[0].reverse()
	b[0].reverse()
	e1="".join(str(e) for e in a[0])
	e2="".join(str(e) for e in b[0])
	d1="".join(str(e) for e in a[1])
	d2="".join(str(e) for e in b[1])
	if a[0][0]=="-":
		e1=int(e1.replace('-',""))
		d1=float('0.'+d1)
		e1=e1*-1
		d1=d1*-1
	else:
		e1=float(e1.replace("+",""))
		d1=float('0.'+d1)
	if b[0][0]=='-': 
		e2=float(e2.replace('-',""))
		d2=float("0."+d2)
		e2=e2*-1
		d2=d2*-1
	else:
		e2=float(e2.replace('+',""))
		d2=float("0."+d2)
		
	a[0].reverse()
	b[0].reverse()
	n1=e1+d1
	n2=e2+d2
	if n1==n2:
		print ('Las tuplas de números son iguales')
	else:
		print ('Las tuplas de números son diferentes')
	return c 
    pass


def pi():
    s = 0
    for i in range(1, n + 1):
        s += ((-1)**(i+1)) / (2*i-1)
        float(s)
    
    return float (4*s)
    pass


if __name__ == "__main__":
print(imprimir(pi()))
