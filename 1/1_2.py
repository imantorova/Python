#coding: utf-8
import os
import math
w_file=open ('E:/Kurs/Spisok.txt','r')
a1=w_file.readline()
a2=w_file.readline()
res_a=int(a1)+int(a2)
print (' Number 1: ',a1,'Number 2: ',a2,'Sum: ',res_a)
b1=w_file.readline()
b2=w_file.readline()
b3=w_file.readline()
res_b=math.sqrt(int(b1)*int(b2))
print (' Number 3: ',b1,'Number 4: ',b2,'Square root: ',res_b)
if res_a>res_b:
    print (' Sum of #1 and #2 > Square root of (#3*#4)',res_a)
else:
    print (' Square root (#3*#4)> Sum #1 and #2',res_b)
b3=w_file.readline()
res_c=math.cos(int(b3))
print (' Cos of number 5',b3,'=',res_c)
