#coding: utf-8
import math
diametr = ['45','338','19']
for j,i in enumerate (diametr):
        Ss=(float (i)**2)/4 
        S_R= math.pi*Ss
        print ('������� ����� � ���������',i, '=',S_R)
        diametr [j]=S_R
print (diametr)
razn=diametr[2]-diametr[1]-diametr[0]
print ('������� 3�� ����� ����� �������� 1�� � 2�� ������=',razn)