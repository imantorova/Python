#coding: utf-8
import math
a=[1,-20,38,0,44]
b=[88,-20,48,4,33,2]
print ('a=',a)
print ('b=',b)
for i in range (0,5):
    if a[i]>b[i]:
        print ('Number a is bigger b',a[i])
    elif a[i]<b[i]:
        print ('Number b is bigger a',b[i])
    else:
        print ('Numbers a and b are equals', a[i],b[i])
for j in range (0,5):
    sred=abs(a[j]-b[j])
    print ('a=',a[j],'b=',b[j],'Raznica me>|<du a i b po modulu =',sred)
    if sred>15:
       print ('Tadaaaaam! Raznica bol"we 15!!!',sred)