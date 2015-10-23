#coding: utf-8

import pickle
import os

FILENAME = 'data.pickle'
kom = 0
k = 1
ind = []
marka_new = []
power_new = []
index_slovo = []
index_slovo_poln = []

try:
    os.path.exists(FILENAME)
    f = open(FILENAME, 'rb')
    data = pickle.load(f)
except:
    data = {
        'cars_marka': ['BMW', 'Audi', 'Ford', 'Volkswagen', 'Volvo', 'Lada','Hunday'],
        'cars_power':['250','144','93','134', '80', '100', '174']
        }
    print (data)

def vopros ():
    return input('Введите команду: ввести (1), вывести (2):')

def marka_a ():
    flag = 1
    while flag > 0:
        marka = input('Введите марку автомобиля: ') 
        if marka.isalpha():
            data['cars_marka'].append(marka)
            flag = 0
        else:
            print('Марка машины должна состоять только из букв!')

def power_a ():
    flag = 1
    while flag > 0:
        power = input('Введите мощность автомобиля: ')
        if power.isdigit():
            data['cars_power'].append(power)
            flag = 0
        else:
            print('Мощность машины должна состоять только из цифр!')

def v_1():
    for j,i in enumerate (data['cars_power']):
        if vybor_pow == 1:
            if int (v_pow) == int(i):
                ind.append(j)                
        elif vybor_pow == 2:
            if int(v_pow) < int(i):
                ind.append(j)
        elif vybor_pow == 3:
            if int(v_pow) > int(i):
                ind.append(j)
            '''
        elif vybor_pow==4:
            if int(v_pow) > int(v_pow_2):
                start = int(v_pow)
                stop = int(v_pow_2)
            else:
                start = int(v_pow_2)
                stop = int(v_pow)
        sort_list=data['cars_power']
        sort_list.sort()
    print (sort_list)
    print (sort_list[start:stop])
    '''
    for i in ind:
        power_new.append (data['cars_marka'][i])
        power_new.append (data['cars_power'][i])
    print ('Условие соответствует следующим машинам:', power_new)


def v_2():
    slovo = str (input ('Введите слово для поиска соответствия (часть слова):'))
    for j,i in enumerate(data['cars_marka']):
        if slovo in i:
            index_slovo.append (j)
    for i in index_slovo:
        print ('Марка ',data['cars_marka'][i],', мощность',data['cars_power'][i])


def v_3():
    slovo=str (input ('Введите слово для поиска соответствия (полное соответствие):'))
    for j,i in enumerate(data['cars_marka']):
        if slovo == i:
            index_slovo_poln.append (j)
    for i in index_slovo_poln:
        print ('Марка ',data['cars_marka'][i],', мощность',data['cars_power'][i])
  
while k > 0:
    kom = int(vopros())
    if kom == 1:
        marka_a()
        power_a()
        f=open(FILENAME, 'wb')
        pickle.dump(data,f)
        f.close()
        print(data)
        k = 0
    elif kom == 2:
        sort_list=data['cars_marka']
        sort_list.sort()
        print('Все марки автомобилей в алфавитном порядке:',sort_list)
        k=0
    else:
        print ('Введена неверная команда.')


print('Поиск/фильтрация')
vybor_pow = int(input('1. Выберите фильтр: конкретное число(1), больше чем(2), меньше чем (3), в промежутке (4)'))
v_pow = str(input('Введите мощность автомобиля: '))
#v_pow_2 = input ('Введите второе значение мощности (для условия (4))')

#По мощности
v_1()

#По вхождению слова в название
v_2()

#По полному соответствию слова
v_3()
