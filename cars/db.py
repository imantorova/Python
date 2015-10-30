#coding: utf-8

import pickle,os,sys

FILENAME = 'data.pickle'

#Проверка на существование файла
        
try:
    os.path.exists(FILENAME)
    pick_load ()
except:
    data = {
        'cars_marka': ['BMW', 'Audi', 'Ford', 'Volkswagen', 'Volvo', 'Lada','Hunday'],
        'cars_power':['250','144','93','134', '80', '100', '174']
        }

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
