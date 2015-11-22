# coding: utf-8

from tkinter import *

def vyvod_v_doc(event):
    print ('1111')

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
        super().__init__('Имя',0,4,2,18,0,6,2)

class otchestvo(Shablon_text):
    def __init__(self):
        super().__init__('Отчество',0,8,2,30,0,10,2)


class data_rogdeniya (Shablon_text):
    def __init__(self):
        super().__init__('дата рождения   ',1,0,3,20,1,3,3)

class mesto_rogdeniya (Shablon_text):
    def __init__(self):
        super().__init__('место рождения',1,6,3,30,1,9,3)

class pass_ser (Shablon_text):
    def __init__(self):
        super().__init__('паспорт серия    ',3,0,3,20,3,3,3)

class pass_nom (Shablon_text):
    def __init__(self):
        super().__init__('номер',3,6,3,30,3,9,3)

class data_vydachy (Shablon_text):
    def __init__(self):
        super().__init__('дата выдачи       ',4,0,3,20,4,3,3)

class kem_vydan (Shablon_text):
    def __init__(self):
        super().__init__('кем выдан ',4,6,3,30,4,9,3)

class adres_reg (Shablon_text):
    def __init__(self):
        super().__init__('адрес прописки   ',5,0,3,81,5,3,9)

class N_kv (Shablon_text):
    def __init__(self):
        super().__init__('№ квартиры        ',6,0,3,12,6,3,1)

class kadastr_N(Shablon_text):
    def __init__(self):
        super().__init__('Кадастровый №',6,5,2,20,6,7,3)

class etag (Shablon_text):
    def __init__(self):
        super().__init__('Этаж     ',6,10,1,13,6,11,1)

class o_S (Shablon_text):
    def __init__(self):
        super().__init__('Общая площадь ',7,0,3,12,7,3,1)

class o_S_balk (Shablon_text):
    def __init__(self):
        super().__init__('  кв.м.;  Общая площадь с балконом',7,4,5,15,7,9,2)
        Label(root, text='кв.м.', font='Arial 10').grid(row=7,column= 11,columnspan= 1)

class S_kuch (Shablon_text):
    def __init__(self):
        super().__init__('Площадь кухни  ',8,0,3,12,8,3,1)

class S_gil (Shablon_text):
    def __init__(self):
        super().__init__('  кв.м.;                     Жилая площадь',8,4,5,15,8,9,2)
        Label(root, text='кв.м.', font='Arial 10').grid(row=8,column= 11,columnspan= 1)

class N_zap_reg (Shablon_text):
    def __init__(self):
        super().__init__('Рег. № записи    ',9,0,3,12,9,3,1)

class data_reg (Shablon_text):
    def __init__(self):
        super().__init__('                             Дата регистрации',9,4,5,15,9,9,2)

class Sum_dog (Shablon_text):
    def __init__(self):
        super().__init__('Сумма договора ',10,0,3,81,10,3,9)

class pol:
    def __init__(self):
        Label(root, text='пол                    ', font='Arial 10').grid(row=2,column= 0,columnspan= 3)
        var=IntVar()
        var.set(1)
        self.rad0 = Radiobutton(root,text="Мужской",variable=var,value=0).grid(row=2,column= 3,columnspan= 2)
        self.rad1 = Radiobutton(root,text="Женский",variable=var,value=1).grid(row=2,column= 5,columnspan= 2)

class But_save:
    def __init__(self):
        self.but=Button(root, text = 'СОХРАНИТЬ',font='Arial 10').grid(row=11,column=11,columnspan= 2)
        #self.but.bind("<Button-1>",print('!!!'))



class zapusk_formy:
    familiya(),imya(),otchestvo()
    data_rogdeniya(),mesto_rogdeniya()
    pol()
    pass_ser(),pass_nom()
    data_vydachy(),kem_vydan()
    adres_reg()
    N_kv(),kadastr_N(),etag()
    o_S(),o_S_balk()
    S_kuch(),S_gil()
    N_zap_reg(),data_reg()
    Sum_dog()
    But_save()


zapusk_formy()

root.mainloop()

'''

'''
