#coding: utf-8
import os, sys,argparse

#Работа с входными параметрами программы

parser = argparse.ArgumentParser()
parser.add_argument('typ',type=str,help='Ввод расширения для поиска файла')
parser.add_argument('path_f',type=str,help='Ввод пути расположения файлов или . для текущей директории')
parser.add_argument('stroka',type=str,help='Ввод искомой подстроки для поиска')
args = parser.parse_args()
print (" Расширение:",args.typ)
print (" Путь:",args.path_f)
print (" Строка поиска:",args.stroka)

#Функция-генератор find

def find (rash):
    for filename in os.listdir(args.path_f):#в текущей директории
        if filename.endswith (rash):
            for i, line in enumerate(open(filename)): #построчно читает
                yield filename,i, line

#Функция-генератор grep

def grep (gen, substr):
    for name, i, s in gen:
        if substr in s:
            yield name, i, s
           
#Выводятся наименование файла; № строки и сама строка(где есть введеная строка для поиска)

for name, i, s  in grep (gen=find (args.typ),substr=args.stroka):
    print(name, i, s)
