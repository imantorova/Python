#coding: utf-8
import os
import math
w_file=open ('E:/Kurs/Spisok.txt','r')
a1=w_file.readline()
a2=w_file.readline()
res_a=int(a1)+int(a2)
print (' ������ �����: ',a1,'������ �����: ',a2,'�����: ',res_a)
b1=w_file.readline()
b2=w_file.readline()
b3=w_file.readline()
res_b=math.sqrt(int(b1)*int(b2))
print (' ������ �����: ',b1,'��������� �����: ',b2,'���������� ������ �� ���������� ���������: ',res_b)
if res_a>res_b:
    print (' ����� ������ ���� ����� ������,��� ���������� ������ �� ���������� ��������� �������� � ���������� �����',res_a)
else:
    print (' ���������� ������ �� ���������� ��������� �������� � ���������� ����� ������ ��� ����� ����� ������� � �������',res_b)
b3=w_file.readline()
res_c=math.cos(int(b3))
print (' ������� �� ������ �����',b3,'=',res_c)
