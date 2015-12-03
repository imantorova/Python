# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5. QtWidgets import QMessageBox
 
class Forma(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):
        self.resize(634, 379)
        self.setGeometry(QtCore.QRect(300, 300, 631, 341))
        self.centralwidget = QtWidgets.QWidget(self)
        self.setWindowTitle('Программа для автозаполнения документов')

        #надписи
        self.l_lst={
            'text':["Фамилия","имя","отчество", "место рождения", "паспорт: серия",
                    "номер","кем выдан","адрес регистрации","№ квартиры","этаж","площадь квартиры с балконом",
                    "площадь квартиры", "жилая площадь","площадь кухни","Кадастровый номер","Запись регистрации",
                    "Сумма договора","дата рождения","пол","количество комнат","когда выдан","дата регистрации","руб."],
            'x':[2,210,400,179,2,220,2,2,2,190,2,208,365,500,2,2,2,2,456,337,462,441,440],
            'y':[0,0,0,30,60,60,90,120,150,150,180,180,180,180,210,240,270,30,30,150,60,240,270],
            'width':[44,18,47,83,77,30,54,97,66,25,158,102,81,82,102,102,82,79,18,98,66,92,31],
            'height':[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16]
            }
        for i in range (23):
                    
            self.label = QtWidgets.QLabel(self)
            self.label.setGeometry(QtCore.QRect(self.l_lst['x'][i], self.l_lst['y'][i], self.l_lst['width'][i], self.l_lst['height'][i]))
            self.label.setText(self.l_lst['text'][i])

                
        #поля ввода текста
        self.e_lst={
            'x':[53,240,459,270,85,270,84,105,74,221,163,315,455,584,110,110,110],
            'y':[0,0,0,30,60,60,90,120,150,150,180,180,180,180,210,240,270],
            'width':[141,141,161,171,111,171,541,521,110,110,41,41,41,41,321,321,321],
            'height':[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20]

            }    
        self.lE_lst=[]
        for i in range (17):
        
            self.lineEdit = QtWidgets.QLineEdit(self)
            self.lineEdit.setGeometry(QtCore.QRect(self.e_lst['x'][i], self.e_lst['y'][i], self.e_lst['width'][i], self.e_lst['height'][i]))
            self.lE_lst.append(self.lineEdit)

        #переключатели для типа "пол"
        self.radioButton = QtWidgets.QRadioButton(self)
        self.radioButton.setGeometry(QtCore.QRect(480, 30, 66, 18))
        self.radioButton.setText("мужской")
        self.radioButton.clicked.connect(lambda *args: self.showDialog3(1))
        
        self.radioButton_2 = QtWidgets.QRadioButton(self)
        self.radioButton_2.setGeometry(QtCore.QRect(552, 30, 66, 18))
        self.radioButton_2.setText("женский")
        self.radioButton_2.clicked.connect(lambda *args: self.showDialog3(2))
       
        
        #объединение в группу переключателей
        self.buttonGroup = QtWidgets.QButtonGroup(self)
        self.buttonGroup.addButton(self.radioButton)
        self.buttonGroup.addButton(self.radioButton_2)

        #-------
        #переключатели для типа "количество комнат"
        self.radioButton_3 = QtWidgets.QRadioButton(self)
        self.radioButton_3.setGeometry(QtCore.QRect(441, 150, 29, 18))
        self.radioButton_3.setText("1")
        self.radioButton_3.clicked.connect(lambda *args: self.showDialog4(1))
        
        
        self.radioButton_4 = QtWidgets.QRadioButton(self)
        self.radioButton_4.setGeometry(QtCore.QRect(476, 150, 29, 18))
        self.radioButton_4.setText("2")
        self.radioButton_4.clicked.connect(lambda *args: self.showDialog4(2))

        self.radioButton_5 = QtWidgets.QRadioButton(self)
        self.radioButton_5.setGeometry(QtCore.QRect(511, 150, 29, 18))
        self.radioButton_5.setText("3")
        self.radioButton_5.clicked.connect(lambda *args: self.showDialog4(3))

        #объединение в группу переключателей
        self.buttonGroup_2 = QtWidgets.QButtonGroup(self)
        self.buttonGroup_2.addButton(self.radioButton_3)
        self.buttonGroup_2.addButton(self.radioButton_4)
        self.buttonGroup_2.addButton(self.radioButton_5)

        
        #поле типа дата        
        self.dateEdit=QtWidgets.QDateEdit(self)
        self.dateEdit.setGeometry(QtCore.QRect(86, 30, 85, 20))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(1900, 1, 1)))
   
        self.dateEdit_2 = QtWidgets.QDateEdit(self)
        self.dateEdit_2.setGeometry(QtCore.QRect(534, 60, 85, 20))
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1)))
        
        self.dateEdit_3 = QtWidgets.QDateEdit(self)
        self.dateEdit_3.setGeometry(QtCore.QRect(539, 240, 85, 20))
        self.dateEdit_3.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 1, 1)))


        self.pushButton = QtWidgets.QPushButton("Проверить",self)
        self.pushButton.setGeometry(QtCore.QRect(430, 310, 75, 23))
        self.pushButton.clicked.connect(self.showDialog)

        self.pushButton_2 = QtWidgets.QPushButton("Сохранить",self)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 310, 75, 23))
        self.pushButton_2.clicked.connect(self.showDialog2)

        self.show()

        
        
    def showDialog(self,text):
        self.text_lst = []
        for i in range (17):
            self.text=self.lE_lst[i].text()
            self.text_lst.append(self.text)
        print(self.text_lst)
        for i in (0,1,2,3):
            if self.text_lst[i].isalpha()==False:
                self.reply = QtWidgets.QMessageBox.question(self, 'Ошибка!'
                                                                  'Поле введено неверно! '
                                                                  'Должны быть только буквы!',self.l_lst['text'][i], QMessageBox.Yes)

        for i in (4,5,8,9,10,11,12,13,16):
            if self.text_lst[i].isdigit()==False:
                self.reply2 = QtWidgets.QMessageBox.question(self, 'Ошибка!'
                                                                  'Поле введено неверно! '
                                                                  'Должны быть только цифры!',self.l_lst['text'][i], QMessageBox.Yes)


    def showDialog2(self,text):
        self.text_lst_2 = []
        self.text_1=self.dateEdit.text()
        self.text_lst_2.append(self.text_1)
        self.text_2=self.dateEdit_2.text()
        self.text_lst_2.append(self.text_2)
        self.text_3=self.dateEdit_3.text()
        self.text_lst_2.append(self.text_3)
        print(self.text_lst_2)

    def showDialog3(self,i):
        self.text_lst_3 = []
        if i==1:
            self.text_lst_3.append('мужской')
        elif i==2:
            self.text_lst_3.append('женский')

        print(self.text_lst_3)    

    def showDialog4(self,i):
        self.text_lst_4 = []
        if i==1:
            self.text_lst_4.append('1')
        elif i==2:
            self.text_lst_4.append('2')    
        elif i==3:
            self.text_lst_4.append('3')

        print(self.text_lst_4)
        
   
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    forma = Forma()
    sys.exit(app.exec_())
