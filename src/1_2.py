#coding: utf-8
import os
import math
w_file=open ('E:/Kurs/Spisok.txt','r')
a1=w_file.readline()
a2=w_file.readline()
res_a=int(a1)+int(a2)
print (' Первое число: ',a1,'Второе число: ',a2,'Сумма: ',res_a)
b1=w_file.readline()
b2=w_file.readline()
b3=w_file.readline()
res_b=math.sqrt(int(b1)*int(b2))
print (' Третье число: ',b1,'Четвертое число: ',b2,'Квадратный корень от результата умножения: ',res_b)
if res_a>res_b:
    print (' Сумма первых двух чисел больше,чем квадратный корень от результата умножения третьего и четвертого чисел',res_a)
else:
    print (' Квадратный корень от результата умножения третьего и четвертого чисел больше чем сумма чисел первого и второго',res_b)
b3=w_file.readline()
res_c=math.cos(int(b3))
print (' Косинус от пятого числа',b3,'=',res_c)
