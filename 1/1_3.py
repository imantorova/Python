#coding: utf-8
import math
diametr = ['45','338','19']
for j,i in enumerate (diametr):
        Ss=(float (i)**2)/4 
        S_R= math.pi*Ss
        print ('S kruga s diametrom',i, '=',S_R)
        diametr [j]=S_R
print (diametr)
razn=diametr[2]-diametr[1]-diametr[0]
print ('Diametr 3go kruga - diametry 1go i 2go krugov=',razn)