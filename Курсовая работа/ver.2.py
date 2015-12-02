# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
 
class Forma(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):
        self.resize(634, 379)
        self.setGeometry(QtCore.QRect(0, 10, 631, 341))
        self.centralwidget = QtWidgets.QWidget(self)


        #надписи
        self.l_lst={
            'text':["Фамилия","имя","отчество","дата рождения", "место рождения", "пол","количество комнат","паспорт: серия",
                    "номер","когда выдан","кем выдан","этаж","№ квартиры","адрес регистрации","площадь квартиры","площадь кухни",
                    "площадь квартиры с балконом","жилая площадь","Кадастровый номер","Запись регистрации","дата регистрации",
                    "Сумма договора","руб."],
            'x':[2,210,400,2,179,456,337,2,220,462,2,190,2,2,208,500,2,365,2,2,441,2,440],
            'y':[0,0,0,30,30,30,150,60,60,60,90,150,150,120,180,180,180,180,210,240,240,270,270],
            'width':[44,18,47,79,83,18,98,77,30,66,54,25,66,97,102,82,158,81,102,102,92,82,31],
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

        for i in range (17):
        
            self.lineEdit = QtWidgets.QLineEdit(self)
            self.lineEdit.setGeometry(QtCore.QRect(self.e_lst['x'][i], self.e_lst['y'][i], self.e_lst['width'][i], self.e_lst['height'][i]))

        #переключатели для типа "пол"
        self.radioButton = QtWidgets.QRadioButton(self)
        self.radioButton.setGeometry(QtCore.QRect(480, 30, 66, 18))
        self.radioButton.setText("мужской")
        
        self.radioButton_2 = QtWidgets.QRadioButton(self)
        self.radioButton_2.setGeometry(QtCore.QRect(552, 30, 66, 18))
        self.radioButton_2.setText("женский")
        
        #объединение в группу переключателей
        self.buttonGroup = QtWidgets.QButtonGroup(self)
        self.buttonGroup.addButton(self.radioButton)
        self.buttonGroup.addButton(self.radioButton_2)

        #-------
        #переключатели для типа "количество комнат"
        self.radioButton_3 = QtWidgets.QRadioButton(self)
        self.radioButton_3.setGeometry(QtCore.QRect(441, 150, 29, 18))
        self.radioButton_3.setText("1")
        
        self.radioButton_4 = QtWidgets.QRadioButton(self)
        self.radioButton_4.setGeometry(QtCore.QRect(476, 150, 29, 18))
        self.radioButton_4.setText("2")

        self.radioButton_5 = QtWidgets.QRadioButton(self)
        self.radioButton_5.setGeometry(QtCore.QRect(511, 150, 29, 18))
        self.radioButton_5.setText("3")

        #объединение в группу переключателей
        self.buttonGroup_2 = QtWidgets.QButtonGroup(self)
        self.buttonGroup_2.addButton(self.radioButton_3)
        self.buttonGroup_2.addButton(self.radioButton_4)
        self.buttonGroup_2.addButton(self.radioButton_5)

        
        #поле типа дата        
        self.dateEdit = QtWidgets.QDateEdit(self)
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
        self.pushButton_2.clicked.connect(self.showDialog)

        self.show()

        
        
    def showDialog(self,text):
        self.text=self.dateEdit.text()
        print('123',self.text)
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    forma = Forma()
    sys.exit(app.exec_())
