#coding: utf-8

import pickle,os,sys

FILENAME = 'data.pickle'
kom = 0
k = 1
ind = []
udal=[]
data_new = []
marka_new = []
power_new = []
index_slovo = []
index_slovo_poln = []

#Проверка на существование файла
        
try:
    os.path.exists(FILENAME)
    pick_load ()
except:
    data = {
        'cars_marka': ['BMW', 'Audi', 'Ford', 'Volkswagen', 'Volvo', 'Lada','Hunday'],
        'cars_power':['250','144','93','134', '80', '100', '174']
        }

print (data)

    

#П. 1.3 задания 4 (Ввести и Вывести - 2 отдельные функции)

def input_func():
    return input ()

def output_func(*args):
    return print(*args)

#П. 1.1 задания 4 (ввод команды - отдельная функция)

def vopros ():
    output_func('Введите команду: ввести (1), вывести (2):')
    return input_func ()

def marka_a ():
    flag = 1
    while flag > 0:
        output_func('Введите марку автомобиля: ')
        marka = input_func() 
        if marka.isalpha():
            data['cars_marka'].append(marka)
            flag = 0
        else:
            output_func('Марка машины должна состоять только из букв!')


def power_a ():
    flag = 1
    while flag > 0:
        output_func('Введите мощность автомобиля: ')
        power = input_func()
        if power.isdigit():
            data['cars_power'].append(power)
            flag = 0
        else:
            output_func('Мощность машины должна состоять только из цифр!')

#П. 1.4 задания 4 (все функции сортировки)
#По мощности - конкретное число, больше, меньше, в промежутке
            
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
        elif vybor_pow==4:
            if int(v_pow) < int(v_pow_2):
                start = int(v_pow)
                stop = int(v_pow_2)
            else:
                start = int(v_pow_2)
                stop = int(v_pow)
            if start < int(i):
                ind.append(j)
                if int (i) > stop:
                    ind.remove (j)
    if ind == []:
        output_func ('Таких элементов нет.')
    for i in ind:
        power_new.append (data['cars_marka'][i])
        power_new.append (data['cars_power'][i])
    output_func('Условие соответствует следующим машинам:', power_new)

#По вхождению слова в название
    
def v_2():
    output_func('Введите слово для поиска соответствия (часть слова):')
    slovo = str (input_func ())
    if slovo.isalpha():
        if len (slovo) > 0:
            for j,i in enumerate(data['cars_marka']):
                if slovo in i:
                    index_slovo.append (j)
                    for i in index_slovo:
                        output_func('Марка ',data['cars_marka'][i],', мощность',data['cars_power'][i])
    else:
        output_func('Не введено ни одного значения или совпадений нет')
        
#По полному соответствию слов
        
def v_3():
    output_func('Введите слово для поиска соответствия (полное соответствие):')
    slovo=str (input_func ())
    if slovo.isalpha():
        if slovo in data['cars_marka']:
            for j,i in enumerate(data['cars_marka']):
                 if slovo == i:
                    index_slovo_poln.append (j)
            for i in index_slovo_poln:
                output_func('Марка ',data['cars_marka'][i],', мощность',data['cars_power'][i])
        elif slovo not in data['cars_marka']:
            output_func('Нет соответствий')
    else:
        output_func('Не введено ни одного значения')
        

#П. 1.5 задания 4
#выгрузка из pickle
def pick_load ():
    f = open(FILENAME, 'rb')
    data = pickle.load(f)

#загрузка из pickle
def pick_dump():
        f=open(FILENAME, 'wb')
        pickle.dump(data,f)
        f.close()

#Редактирование 
def red_cars ():
    for j,i in enumerate (data['cars_marka']):
        if r_car == i:
            ind.append(j)
            continue
        elif r_car == i:
            output_func('Неверно введено наименование машины')
            break
    for i in ind:
        output_func('Введите новое наименование машины')
        k = input_func()
        data['cars_marka'].insert(i,k)
        data['cars_marka'].pop(i+1)
        output_func('Введите новое значение мощности')
        k = input_func()
        data['cars_power'].insert(i,k)
        data['cars_power'].pop(i+1)
        break
    output_func (data['cars_marka'][i],data['cars_power'][i])

#Удаление
def udal_cars():
    for j,i in enumerate (data['cars_marka']):
        if r_car == i:
            udal.append(j)
    for i in udal:
        output_func('Удаление данных')
        data['cars_marka'].pop(i)
        data['cars_power'].pop(i)
    output_func (data)
    
#П 2. Улучшаем: 
#функции Ввести и Вывести добавляем в словарь следующим образом:
#FUNCS = {
#'ввести': input_func,
#'вывести': output_func,
#}
#И меняем if-else на поиск в этом словаре и запуск функции по ключу словаря.
            
FUNCS = {
'ввести': input_func,
'вывести': output_func,
}

#П. 1 задания 3

while k > 0:
    kom = int(vopros())
    if kom == 1:
        marka_a()
        power_a()
        pick_dump()
#использование FUNCS вывод данных
        if 'вывести' in FUNCS:
            FUNCS['вывести'](data)
        k = 0
    elif kom == 2:
        for j,i in enumerate (data['cars_marka']):
            data_new.append([data['cars_marka'][j],data['cars_power'][j]])
        data_new.sort()
        output_func('Все марки автомобилей в алфавитном порядке:',data_new)
        k=0
    else:
        if 'вывести' in FUNCS:
            FUNCS['вывести']('Введена неверная команда.')
        
#П. 2 задания 3

output_func('Поиск/фильтрация')
output_func('1. Выберите фильтр: конкретное число(1), больше чем(2), меньше чем (3), в промежутке (4)')
 
#использование FUNCS ввод данных 

if 'ввести' in FUNCS:
    vybor_pow = int(FUNCS['ввести']())
    output_func('Введите мощность автомобиля: ')
if 'ввести' in FUNCS:
    v_pow = str(FUNCS['ввести']())
    output_func('Введите второе значение мощности (для условия (4))')
if 'ввести' in FUNCS:
    v_pow_2 = str(FUNCS['ввести']())
    
#По мощности
v_1()

#По вхождению слова в название
v_2()

#По полному соответствию слова
v_3()

output_func('Редактирование/удаление')
output_func('1. Выберите действие: редактирование(1) или удаление (2)')

#Обработка исключения ValueError

try:
    vybor_red = int(input_func())
except ValueError:
    output_func ('Неверное значение!')
finally:
    pass


if vybor_red==1:
    output_func('Введите наименование машины для внесения изменений')
    r_car = input_func()
    i=data['cars_marka'].index (r_car)
    output_func (data['cars_marka'][i],data['cars_power'][i])
    pick_load ()
    red_cars ()
    pick_dump()
elif vybor_red==2:
    output_func('Введите наименование машины для удаления')
    r_car = input_func()
    i=data['cars_marka'].index (r_car)
    output_func (data['cars_marka'][i],data['cars_power'][i])
    pick_load ()
    udal_cars ()
    pick_dump()
else:
    output_func('Введена неверная команда.')
