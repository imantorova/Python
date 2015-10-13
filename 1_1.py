#coding: utf-8
import os
list=os.listdir('E:/Kurs')
w_file=open ('E:/Kurs/result.txt','w')
for i in list:
    a=open(i,'r')
    data = a.read()
    b=data.count ('python')

    if (b>0):
        print ('File name: ',i,';  Sum of "python": ',b)
        w_file.write('File name: ')
        w_file.write(i)
        w_file.write(';  Sum of "python": ')
        w_file.write(str(b))
        w_file.write('\n')
w_file.close()
