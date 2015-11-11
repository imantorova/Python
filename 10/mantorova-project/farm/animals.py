#coding: utf-8

import random

a = int (input ('Введите количество уток: '))
b = int (input ('Введите количество коров: '))
c = int (input ('Введите количество собак: '))

def itog_all (x):
      
    status_run = []
    status_voice = []
    status_usef = []
    s = [0,0,0]
        
    for i in x :
        status_run.append(i.aMdist)
        status_voice.append(i.aMvoice_use)
        status_usef.append(i.aMusefulness_proz)
          
    for j,i in enumerate (status_run):
        s[0] += status_run [j]
        s[1] += status_voice [j]
        s[2] += status_usef [j]

    print ('Все животные за месяц: ',' \nобщий пробег (м) - ', s[0], ', \nобщее число раз подачи голоса (раз) - ', s[1],', \nобщее число полученного продукта  - ',s[2])


def itog_all_s (x):
      
    status_run = []
    status_voice = []
    status_usef = []
    s = [0,0,0]
        
    for i in x :
        status_run.append(i.aMdist)
        status_voice.append(i.aMvoice_use)
        status_usef.append(i.aMusefulness_proz)
          
    for j,i in enumerate (status_run):
        s[0] += status_run[j]
        s[1] += status_voice[j]
        s[2] += status_usef[j]

    print ('Все животные за месяц: ',' \nобщий пробег (м) - ', s[0], ', \nобщее число раз подачи голоса (раз) - ', s[1],', \nсредняя безопасность на ферме в %  - ',s[2]/c)



class Animal:
    
    def __init__(self,dist,voice,voice_use,usefulness,usefulness_proz):
        self.dist = dist
        self.voice = voice
        self.voice_use = voice_use
        self.usefulness = usefulness        

        
		
class Duck(Animal):

    def __init__(self):
        
        self.dist = random.randint(1,10)
        self.voice = 'Кря'
        self.voice_use =random.randint(0,100)
        self.usefulness = 'Яйцо'
        self.usefulness_proz=random.randint(1,3)
        self.aMdist=self.dist*30
        self.aMvoice_use=self.voice_use*30
        self.aMusefulness_proz=self.usefulness_proz*30


    def status (self):
        
        print ('Пройдено за день (метров):',self.dist,', \nголос:',self.voice,',\nкрякала за день раз:',self.voice_use,', \nпольза:',self.usefulness,', \nколичество:',self.usefulness_proz)

    def status_aM (self):
        
        print ('\nПройдено за месяц (метров):',self.aMdist,',\nкрякала за месяц раз:',self.aMvoice_use,', \nколичество яиц за месяц:',self.aMusefulness_proz)
     
      
class Cow(Animal):
    
    def __init__(self):
        
        self.dist = random.randint(1,20)
        self.voice = 'Му'
        self.voice_use =random.randint(0,100)
        self.usefulness = 'Молоко'
        self.usefulness_proz=random.randint(5,10)        
        self.aMdist=self.dist*30
        self.aMvoice_use=self.voice_use*30
        self.aMusefulness_proz=self.usefulness_proz*30
        
    def status (self):

        print ('Пройдено за день (метров):',self.dist,', \nголос:',self.voice,',\nмычала за день раз:',self.voice_use,', \nпольза:',self.usefulness,', \nколичество:',self.usefulness_proz)

    def status_aM (self):
        
        print ('\nПройдено за месяц (метров):',self.aMdist,',\nмычала за месяц раз:',self.aMvoice_use,', \nколичество молока за месяц:',self.aMusefulness_proz)

            
        
        
class Dog(Animal):
    
    def __init__(self):
        
        self.dist = random.randint(10,50)
        self.voice = 'Гав'
        self.voice_use = random.randint(0,100)
        self.usefulness = 'Безопасность'
        self.usefulness_proz=random.randint(0,100)       
        self.aMdist=self.dist*30
        self.aMvoice_use=self.voice_use*30
        self.aMusefulness_proz=self.usefulness_proz
        
    def status (self):
        
        print ('Пройдено за день (метров):',self.dist,', \nголос:',self.voice,',\nгавкала за день раз:',self.voice_use,', \nпольза:',self.usefulness,', \n% защиты территории:',self.usefulness_proz)

    def status_aM (self):
        
        print ('\nПройдено за месяц (метров):',self.aMdist,',\nпрогавкала за месяц раз:',self.aMvoice_use,', \nсредняя безопасность в % за месяц:',self.aMusefulness_proz)
        
       

class Farm:
    
    animals = {}
    ducks=[]
    dogs=[]
    cows=[]
    
    
    def __init__(self):
        
        self.animals={'ducks':self.ducks,'cows':self.cows,'dogs':self.dogs}
        
        for i in range(a):
            self.animals['ducks'].append(Duck())
            
        for i in range(b):
            self.animals['cows'].append(Cow())
            
        for i in range(c):
            self.animals['dogs'].append(Dog())

    def afterMonth(self):

        #Утки
            
        for j, i in enumerate (self.animals ['ducks']):
            print ('\nУтка № ',j+1)
            i.status ()
            i.status_aM ()

        #Коровы            
            
        for j, i in enumerate (self.animals ['cows']):
            print ('\nКорова № ',j+1)
            i.status ()
            i.status_aM ()

        #Собаки            
            
        for j, i in enumerate (self.animals ['dogs']):
            print ('\nСобака № ',j+1)
            i.status ()
            i.status_aM ()
            
    def itog (self):

        print ('\nСводная информация:\n','\nУтки:')

        itog_all(self.animals ['ducks'])
        
        print ('\nКоровы:')
        
        itog_all(self.animals ['cows'])
                                         
        print ('\nСобаки:')
        
        itog_all_s(self.animals ['dogs'])
                                         
         
if __name__ == '__main__':           


    farm = Farm ()
    farm.afterMonth ()
    farm.itog ()






