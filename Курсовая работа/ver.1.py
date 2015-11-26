# coding: utf-8

from tkinter import *

def vyvod_v_doc(event):
    print ('1111')
    print(inputs.save_from())

root=Tk()

class Shablon_text_label:
    def __init__(self,text,r1,c1,cs1):
        Label(root, text=text, font='Arial 10').grid(row=r1,column= c1,columnspan= cs1)

class Shablon_text_input:
    def __init__(self,w,r2,c2,cs2):
        self.e=Entry(root,width=w,bd=2)
        self.e.grid(row=r2,column=c2,columnspan=cs2)

class labels(Shablon_text_label):
    def __init__(self):
        l={'name':['Фамилия','Имя','Отчество','дата рождения   ','место рождения','паспорт серия    ','номер','дата выдачи       ',
                  'кем выдан ','адрес прописки   ','№ квартиры        ','Кадастровый №','Этаж     ','Общая площадь ',
                  '  кв.м.;  Общая площадь с балконом','Площадь кухни  ','  кв.м.;                     Жилая площадь',
                  'Рег. № записи    ','                             Дата регистрации','Сумма договора ','пол                    '],
            'lab_row':[0,0,0,1,1,3,3,4,4,5,6,6,6,7,7,8,8,9,9,10,2],
            'lab_column':[0,4,8,0,6,0,6,0,6,0,0,5,10,0,4,0,4,0,4,0,0],
            'lab_columnspan':[2,2,2,3,3,3,3,3,3,3,3,2,1,3,5,3,5,3,5,3,3]
        }
        for i in range (21):
            super().__init__(l['name'][i],l['lab_row'][i],l['lab_column'][i],l['lab_columnspan'][i])

class inputs(Shablon_text_input):
    def __init__(self):
        #буквы!
        i_bukva={'dl_bukva':[20,18,30,30],
                 'i_bukva_row':[0,0,0,1],
                 'i_bukva_column':[2,6,10,9],
                 'i_bukva_columnspan':[2,2,2,3]
        }
        b_lst=[]
        for i in range (4):
            self.buk=super().__init__(i_bukva['dl_bukva'][i],i_bukva['i_bukva_row'][i],
                             i_bukva['i_bukva_column'][i],i_bukva['i_bukva_columnspan'][i])
            b_lst.append(self.buk)
        print (b_lst)

        #цифры!
        i_cifra={'dl_cifra':[20,30,20,12,13,12,15,12,15,81],
                 'i_cifra_row':[3,3,4,6,6,7,7,8,8,10],
                 'i_cifra_column':[3,9,3,3,11,3,9,3,9,3],
                 'i_cifra_columnspan':[3,3,3,1,1,1,2,1,2,9]
        }
        c_lst=[]
        for i in range (10):
            self.cif=super().__init__(i_cifra['dl_cifra'][i],i_cifra['i_cifra_row'][i],
                             i_cifra['i_cifra_column'][i],i_cifra['i_cifra_columnspan'][i])
            c_lst.append(self.cif)
        print (c_lst)
        #буквы и цифры
        i_b_c={'dl_b_c':[20,30,81,15],
                 'i_b_c_row':[1,4,5,9],
                 'i_b_c_column':[3,9,3,9],
                 'i_b_c_columnspan':[3,3,9,2]
        }
        b_c_lst=[]
        for i in range (4):
            self.b_c=super().__init__(i_b_c['dl_b_c'][i],i_b_c['i_b_c_row'][i],
                             i_b_c['i_b_c_column'][i],i_b_c['i_b_c_columnspan'][i])
            b_c_lst.append(self.b_c)
        print (b_c_lst)
        #не проверить
        ost={'dl':[20,12],'o_row':[6,9],'o_column':[7,3],'o_columnspan':[3,1]}
        for i in range (2):
            self.ostaln=super().__init__(ost['dl'][i],ost['o_row'][i],
                                         ost['o_column'][i],ost['o_columnspan'][i])
'''
    def save_from(x):
        self.x.get()
        print(self.x.get())
'''
class pol:
    def __init__(self):
        var=IntVar()
        var.set(1)
        self.rad0 = Radiobutton(root,text="Мужской",variable=var,value=0).grid(row=2,column= 3,columnspan= 2)
        self.rad1 = Radiobutton(root,text="Женский",variable=var,value=1).grid(row=2,column= 5,columnspan= 2)

class But_save:
    def __init__(self):
        self.but=Button(root, text = 'СОХРАНИТЬ',font='Arial 10')
        self.but.grid(row=11,column=11,columnspan= 2)
        self.but.bind("<Button-1>",vyvod_v_doc)



class zapusk_formy:
    labels()
    inp=inputs()
    pol()
    But_save()
    Label(root, text='кв.м.', font='Arial 10').grid(row=7,column= 11,columnspan= 1)
    Label(root, text='кв.м.', font='Arial 10').grid(row=8,column= 11,columnspan= 1)


zapusk_formy()

root.mainloop()

