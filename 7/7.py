# coding: utf-8
import sys, os

cars=[]

class tank:
    def __init__(self):
        self.model = str(input('Введите модель танка:'))
        self.shassi = bool(input('Есть ли шасси (если нет-Enter):'))
        self.gus = bool(input('Есть ли гусеницы (если нет-Enter):'))
        self.skorost=int(input('Введите скорость танка:'))

    def status (self):
        print (self.model, self.shassi,self.gus,self.skorost)

class mashina:
    def __init__(self):
        self.model = str(input('Введите модель машины:'))
        self.kolesa = int(input('Введите количество колес машины:'))
        self.skorost=int(input('Введите скорость машины:'))

    def status (self):
        print (self.model, self.kolesa,self.skorost)

class telega:
    def __init__(self):
        self.kolesa = int(input('Введите количество колес телеги:'))
        self.skorost=int(input('Введите скорость телеги:'))

    def status (self):
        print (self.kolesa,self.skorost)

Tank_1=tank()
Mash_1=mashina()
Telega_1=telega()
cars.append (Tank_1)
cars.append (Mash_1)
cars.append (Telega_1)
Tank_2=tank()
Mash_2=mashina()
Telega_2=telega()
cars.append (Tank_2)
cars.append (Mash_2)
cars.append (Telega_2)

for i in cars:
    print (i.status())

def izmenenie ():
    k='go'
    while k!='stop':
        vybor = int(input('Введите тип транспортного средства для изменения параметров: 1-танк, 2-машина,3-телега'))
        naimen = input ('Введите наименование модели, в которой будут произведены изменения (для танка или машины) или количество колес для телеги:')

        if vybor==1:
            izm = int(input ('Введите параметр, который Вы хотите изменить: 1-модель,2-наличие шасси,3-наличие гусениц,4-скорость'))
            if izm==1:
                if Tank_1.model==naimen:
                    Tank_1.model=input ('Введите новое наименование для танка')
                    print (Tank_1.status())
                if Tank_2.model==naimen:
                    Tank_2.model=input ('Введите новое наименование для танка')
                    print (Tank_2.status())
            if izm==2:
                if Tank_1.model==naimen:
                    Tank_1.shassi=bool(input ('Введите новое значение для шасси'))
                    print (Tank_1.status())
                if Tank_2.model==naimen:
                    Tank_2.shassi=bool(input ('Введите новое значение для шасси'))
                    print (Tank_2.status())
            if izm==3:
                if Tank_1.model==naimen:
                    Tank_1.gus=bool(input ('Введите новое значение для гусениц'))
                    print (Tank_1.status())
                if Tank_2.model==naimen:
                    Tank_2.gus=bool(input ('Введите новое значение для гусениц'))
                    print (Tank_2.status())
            if izm==4:
                if Tank_1.model==naimen:
                    Tank_1.skorost=int (input ('Введите новое значение для скорости'))
                    print (Tank_1.status())
                if Tank_2.model==naimen:
                    Tank_2.skorost=int (input ('Введите новое значение для скорости'))
                    print (Tank_2.status())

                
        if vybor==2:
            izm = int(input ('Введите параметр, который Вы хотите изменить: 1-модель,2-количество колес,3-скорость'))
            if izm==1:
                if Mash_1.model==naimen:
                    Mash_1.model=input ('Введите новое наименование для машины')
                    print (Mash_1.status())
                if Mash_2.model==naimen:
                    Mash_2.model=input ('Введите новое наименование для машины')
                    print (Mash_2.status())
            if izm==2:
                if Mash_1.model==naimen:
                    Mash_1.kolesa=int(input ('Введите новое значение для количества колес'))
                    print (Mash_1.status())
                if Mash_2.model==naimen:
                    Mash_2.kolesa=int(input ('Введите новое значение для количества колес'))
                    print (Mash_2.status())
            if izm==3:
                if Mash_1.model==naimen:
                    Mash_1.skorost=int (input ('Введите новое значение для скорости'))
                    print (Mash_1.status())
                if Mash_2.model==naimen:
                    Mash_2.skorost=int (input ('Введите новое значение для скорости'))
                    print (Mash_2.status())
        if vybor==3:
            izm = int(input ('Введите параметр, который Вы хотите изменить: 1-количество колес,2-скорость'))
            if izm==1:
                if Telega_1.kolesa==int(naimen):
                    Telega_1.kolesa=int(input ('Введите новое значение для количества колес'))
                    print (Telega_1.status())
                if Telega_2.kolesa==int(naimen):
                    Telega_2.kolesa=int(input ('Введите новое значение для количества колес'))
                    print (Telega_2.status())
            if izm==2:
                if Telega_1.kolesa==int(naimen):
                    Telega_1.skorost=int(input ('Введите новое значение для скорости'))
                if Telega_2.kolesa==int(naimen):
                    Telega_2.skorost=int(input ('Введите новое значение для скорости'))
                    print (Telega_2.status())
        k=input ('Для завершения ввода изменений введите stop')

izmenenie ()

for i in cars:
    print (i.status())
