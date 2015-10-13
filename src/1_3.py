#coding: utf-8
import math
diametr = ['45','338','19']
for j,i in enumerate (diametr):
        Ss=(float (i)**2)/4 
        S_R= math.pi*Ss
        print ('Площадь круга с диаметром',i, '=',S_R)
        diametr [j]=S_R
print (diametr)
razn=diametr[2]-diametr[1]-diametr[0]
print ('Диаметр 3го круга минус диаметры 1го и 2го кругов=',razn)