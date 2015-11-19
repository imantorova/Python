# coding: utf-8

from tkinter import *

root=Tk()

class Shablon_text:
    def __init__(self,text,r1,c1,cs1,w,r2,c2,cs2):

        Label(root, text=text, font='Arial 10').grid(row=r1,column= c1,columnspan= cs1)
        Entry(root,width=w,bd=2).grid(row=r2,column=c2,columnspan=cs2)

class familiya(Shablon_text):
    def __init__(self):
        super().__init__('Фамилия',0,0,2,20,0,2,2)

class imya(Shablon_text):
    def __init__(self):
        super().__init__('Имя',0,4,2,20,0,6,2)

class otchestvo(Shablon_text):
    def __init__(self):
        super().__init__('Отчество',0,8,2,20,0,10,2)


class data_rogdeniya (Shablon_text):
    def __init__(self):
        super().__init__('дата рождения ',1,0,3,20,1,3,3)

class mesto_rogdeniya (Shablon_text):
    def __init__(self):
        super().__init__('место рождения',1,6,3,30,1,9,3)

class pass_ser (Shablon_text):
    def __init__(self):
        super().__init__('паспорт серия  ',3,0,3,20,3,3,3)

class pass_nom (Shablon_text):
    def __init__(self):
        super().__init__('номер',3,6,3,30,3,9,3)

class data_vydachy (Shablon_text):
    def __init__(self):
        super().__init__('дата выдачи     ',4,0,3,20,4,3,3)

class kem_vydan (Shablon_text):
    def __init__(self):
        super().__init__('кем выдан ',4,6,3,30,4,9,3)

class adres_reg (Shablon_text):
    def __init__(self):
        super().__init__('адрес прописки ',5,0,3,72,5,3,9)

class N_kv (Shablon_text):
    def __init__(self):
        super().__init__('№ квартиры      ',6,0,3,13,6,3,1)

class kadastr_N(Shablon_text):
    def __init__(self):
        super().__init__('Кадастровый №',6,5,2,20,6,7,3)

class etag (Shablon_text):
    def __init__(self):
        super().__init__('Этаж     ',6,10,1,10,6,11,1)

familiya(),imya(),otchestvo()
data_rogdeniya(),mesto_rogdeniya()
pass_ser(),pass_nom()
data_vydachy(),kem_vydan()
adres_reg()
N_kv(),kadastr_N(),etag()

root.mainloop()

'''
var=IntVar()
var.set(1)
rad0 = Radiobutton(root,text="Мужской",variable=var,value=0)
rad1 = Radiobutton(root,text="Женский",variable=var,value=1)
'''
