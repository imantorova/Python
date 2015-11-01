#coding: utf-8
import os, sys

#Функция-генератор find

def find (rash = '.py'):
    for filename in os.listdir('.'):#в текущей директории
        if filename.endswith (rash):
            for i, line in enumerate(open(filename)): #построчно читает
                yield filename,i, line

#Функция-генератор grep

def grep (gen, substr):
    for name, i, s in gen:
        if substr in s:
            yield name, i, s
            
#Запрос строки для поиска
str_vvod = input ('Введите данные для поиска (подстрока):')

#Выводятся наименование файла; № строки и сама строка(где есть введеная строка для поиска)
for name, i, s  in grep (gen=find ('.py'),substr=str_vvod):
    print(name, i, s)

