#coding: utf-8
import math
def summa(a,b):
    s=float(a)+float(b)
    print ('Сумма чисел',a,'+',b,'=',s)
def minus(a,b):
    mi=float(a)-float(b)
    print ('Разница чисел',a,'-',b,'=',mi)
def delenie(a,b):
    d=float(a)/float(b)
    print ('Число',a,'/',b,'=',d)
def umnogenie(a,b):
    u=float(a)*float(b)
    print ('Произведение',a,'*',b,'=',u)
def stepen(a,b):
    st=float(a)**float(b)
    print (a,'в степени',b,'=',st)
def sinus(a,b):
    sinus_x=sin(float(a))
    sinus_y=sin(float(b))
    print ('Синус',a,'=',sinus_x,';  Синус',b,'=',sinus_y)
def bigger(a,b):
    if float(a)>float(b):
        print (a,'больше',b)
    elif float(a)<float(b):
        print (b,'больше',a)
    else:
        print ('a и b равны')
        
print ('Введите число а и нажмите Enter.')
a=input ()
print ('a=',a)
print ('Введите число b и нажмите Enter.')
b=input ()
print ('b=',b)
print ('Выберите функцию калькулятора: +,-,/,*, **(степень),sin,>(сравнение) и нажмите Enter.')
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