#coding: utf-8
import math
a=[1,-20,38,0,44]
b=[88,-20,48,4,33,2]
print ('a=',a)
print ('b=',b)
for i in range (0,5):
    if a[i]>b[i]:
        print ('Число а больше б',a[i])
    elif a[i]<b[i]:
        print ('Число б больше а',b[i])
    else:
        print ('Числа а и б равны', a[i],b[i])
for j in range (0,5):
    sred=abs(a[j]-b[j])
    print ('a=',a[j],'b=',b[j],'Разница между а и б по модулю =',sred)
    if sred>15:
       print ('Тадаааам! Разница больше 15!!!',sred)