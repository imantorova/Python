#coding: utf-8
import math
def summa(a,b):
    s=float(a)+float(b)
    print ('����� �����',a,'+',b,'=',s)
def minus(a,b):
    mi=float(a)-float(b)
    print ('������� �����',a,'-',b,'=',mi)
def delenie(a,b):
    d=float(a)/float(b)
    print ('�����',a,'/',b,'=',d)
def umnogenie(a,b):
    u=float(a)*float(b)
    print ('������������',a,'*',b,'=',u)
def stepen(a,b):
    st=float(a)**float(b)
    print (a,'� �������',b,'=',st)
def sinus(a,b):
    sinus_x=sin(float(a))
    sinus_y=sin(float(b))
    print ('�����',a,'=',sinus_x,';  �����',b,'=',sinus_y)
def bigger(a,b):
    if float(a)>float(b):
        print (a,'������',b)
    elif float(a)<float(b):
        print (b,'������',a)
    else:
        print ('a � b �����')
        
print ('������� ����� � � ������� Enter.')
a=input ()
print ('a=',a)
print ('������� ����� b � ������� Enter.')
b=input ()
print ('b=',b)
print ('�������� ������� ������������: +,-,/,*, **(�������),sin,>(���������) � ������� Enter.')
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