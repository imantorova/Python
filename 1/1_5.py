#coding: utf-8
import math
def summa(a,b):
    s=float(a)+float(b)
    print ('Summa',a,'+',b,'=',s)
def minus(a,b):
    mi=float(a)-float(b)
    print ('Raznica',a,'-',b,'=',mi)
def delenie(a,b):
    d=float(a)/float(b)
    print ('Rezultat',a,'/',b,'=',d)
def umnogenie(a,b):
    u=float(a)*float(b)
    print ('Proizvedenie',a,'*',b,'=',u)
def stepen(a,b):
    st=float(a)**float(b)
    print (a,'v stepeni',b,'=',st)
def sinus(a,b):
    sinus_x=sin(float(a))
    sinus_y=sin(float(b))
    print ('Sin',a,'=',sinus_x,';  Sin',b,'=',sinus_y)
def bigger(a,b):
    if float(a)>float(b):
        print (a,' bigger ',b)
    elif float(a)<float(b):
        print (b,' bigger ',a)
    else:
        print ('a and b are equals')
        
print ('Vvedite chislo a i nagmite Enter.')
a=input ()
print ('a=',a)
print ('Vvedite chislo b i nagmite Enter.')
b=input ()
print ('b=',b)
print ('Vyberite funcciu kalkuljatora: +,-,/,*, **(stepen"),sin,>(sravnenie) i nagmite Enter.')
znak=input ()
if znak=='+':
    summa (a,b)
if znak=='-':
    minus(a,b)
if znak=='/':
    delenie(a,b)
if znak=='*':
    umnogenie(a,b)
if znak=='**':
    stepen(a,b)    
if znak=='sin':
    sinus(a,b)
if znak=='>':
    bigger(a,b) 