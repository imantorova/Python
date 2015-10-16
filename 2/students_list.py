#coding: utf-8
lst_students=['Ivanov Ilya','Petrov Ivan','Osipov Vadim','Romanov Yuri','Yakovleva Inna','Nikolaev Alexey','Nikoforov Andrey','Nazarova Karina','Fomin Alexey','Demina Olga','Nikitina Inna','Rumyanzeva Nataliya','Golubeva Nataliya','Prokofev Alexey','Smirnov Alexandr','Kamanin Dmitry','Savinova Yulia','Panov Vadim','Belyakov Sergey','Bogdanova Anna']
print (lst_students)
print ('Vvedite familiyu i imya studenta:')
n = input()
f=lst_students.index(n)
print ('Index zapisi=',f)
print ('Vvedite familiyu i imya studenta:')
n1 = input()
f1=lst_students.index(n1)
print ('Index zapisi=',f1)
print ('Vvedite familiyu i imya studenta:')
n2 = input()
f2=lst_students.index(n2)
print ('Index zapisi=',f2)
if f1>f2:
    stop=f1
    start=f2
else:
    stop=f2
    start=f1
srez=lst_students[start:stop]
print (srez)
a=[]
b=[]
f=[]
count=0
lst_students=str(lst_students)
a=(lst_students.split(','))
a=(lst_students.split())
for i in a[0::2]:
    f.append(i)
for i in a[1::2]:
    b.append(i)
for i in b:
    if 'r'in i:
        count=count+1
print ('Kolichestvo imen s bukvoy "r"=',count)
#Zadanie #5 tak i ne poluchilos'
#    if b not in names:
#        names.append(b)
#print (names)
    


