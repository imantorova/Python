#coding: utf-8

import pickle
import os

FILENAME='data.pickle'

try:
    os.path.exists(FILENAME)
    f= open(FILENAME, 'rb')
    data = pickle.load(f)
except:
    data = {
        'cars_marka': ['BMW', 'Audi', 'Ford', 'Volkswagen', 'Volvo', 'Lada','Hunday'],
        'cars_power':['250','144','93','134', '80', '100', '174']
        }
    print (data)

kom=0
k=1

def vopros ():
    return input('Введите команду: ввести (1), вывести (2):')

def marka_a ():
    marka=input('Введите марку автомобиля: ')
    if marka.isalpha():
        data['cars_marka'].append(marka)
        power_a ()
    else:
         print('Марка машины должна состоять только из букв!')
    return ()

def power_a ():
    power=input('Введите мощность автомобиля: ')
    if power.isdigit():
        data['cars_power'].append(power)
        k=0
    else:
        print('Мощность машины должна состоять только из цифр!')
        power_a ()
    return ()

while k>0:
    kom=int(vopros())
    if kom==1:
        marka_a()
        f=open(FILENAME, 'wb')
        pickle.dump(data,f)
        print(data)
        k=0
    elif kom==2:
        sort_list=data['cars_marka']
        sort_list.sort()
        print('Все марки автомобилей в алфавитном порядке:',sort_list)
        k=0
    else:
        print ('Введена неверная команда.')


print('Поиск/фильтрация')
vybor_pow=int(input('Выберите фильтр: конкретное число(1), больше чем(2), меньше чем (3), в промежутке (4)'))
v_pow = str(input('Введите мощность автомобиля: '))

ind=[]

if vybor_pow==1:
    for i in data['cars_power']:
        if v_pow==i:
            ind.append(int(data['cars_power'].index(i)))
    for j in ind:
        print ('Марка автомобиля с мощностью',v_pow,':',data['cars_marka'][ind[j]])

elif vybor_pow==2:
    for i in data['cars_power']:
        if v_pow > i:
            ind.append(int(data['cars_power'].index(i)))
    for j in ind:
        print ('Марка автомобиля с мощностью',v_pow,'больше по мощности, чем',data['cars_marka'][ind[j]],data['cars_power'][ind[j]])

elif vybor_pow==3:
    for i in data['cars_power']:
        if v_pow < i:
            ind.append(int(data['cars_power'].index(i)))
    for j in ind:
        print ('Марка автомобиля с мощностью',v_pow,'меньше по мощности, чем',data['cars_marka'][ind[j]],data['cars_power'][ind[j]])

#else vybor_pow==4:
   # v_pow_2 = str(input('Введите второе значение для мощности автомобиля: '))

