from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QTextEdit, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton

#ЧАСТЬ ИГОРЯ

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.resize(1024,600)
        self.new_text = QtWidgets.QLabel(self)
        self.label = QtWidgets.QLabel(self)
        self.btn = QtWidgets.QPushButton(self)
        self.btn2 = QtWidgets.QPushButton(self)
        self.input_y = QtWidgets.QLineEdit(self)
        self.input_m = QtWidgets.QLineEdit(self)
        self.input_d = QtWidgets.QLineEdit(self)        
    
        self.output = QTextEdit(self)  
        self.UI(self)
        
        
        
    def UI(self, Window):
        
        self.setWindowTitle("Форматы даты")
        self.setGeometry(100, 100, 100, 100)
        self.resize(1024,600)

        self.label.setText("Введите \n данные")
        self.label.move(25, 282)

        self.btn.move(410, 272)
        self.btn.setText("Американский формат")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.resultataAM)
        
        self.btn2.move(410, 332)
        self.btn2.setText("Европейский формат")
        self.btn2.setFixedWidth(200)
        self.btn2.clicked.connect(self.resultataEU)

        self.input_y.move(100, 272)
        self.input_y.resize(300,30)
        self.input_y.setPlaceholderText("Год")

        self.input_m.move(100, 302)
        self.input_m.resize(300,30)
        self.input_m.setPlaceholderText("Месяц")

        self.input_d.move(100, 332)
        self.input_d.resize(300,30)
        self.input_d.setPlaceholderText("День")

        
        self.output.move(620, 272)
        self.output.resize(300,90)
        self.output.setAlignment(QtCore.Qt.AlignCenter)
        
#ЧАСТЬ ЖЕНИ

    def resultataAM(self):
        self.output.clear()
        self.output.setAlignment(QtCore.Qt.AlignCenter)
        self.output.setFontPointSize(32)
        
        self.new_text.setText("Американский формат даты(mm, dd, y)")
        self.new_text.move(620, 250)
        self.new_text.adjustSize()
        
        date = AmericanDate()
        
        date.set_year(int(self.input_y.text()))
        date.set_month(int(self.input_m.text()))
        date.set_day(int(self.input_d.text()))

        self.output.append(str(date.formatAM()))
        
        
    def resultataEU(self):
        self.output.clear()
        self.output.setAlignment(QtCore.Qt.AlignCenter)
        self.output.setFontPointSize(32)
        
        self.new_text.setText("Европейский формат даты(dd, mm, y)")
        self.new_text.move(620, 250)
        self.new_text.adjustSize()

        date = EuropeanDate()
        
        date.set_year(int(self.input_y.text()))
        date.set_month(int(self.input_m.text()))
        date.set_day(int(self.input_d.text()))

        self.output.append(str(date.formatEU()))




class Date:
    def __init__(self, y=0, m=0, d=0):
        self.y = y
        self.m = m
        self.d = d
 
    def get_year(self):
        self.y = str(self.y)
        return self.y
 
    def get_month(self):
        self.m = str(self.m)
        return self.m
 
    def get_day(self):
        self.d = str(self.d)
        return self.d
 
    def set_year(self, ny):
        self.y = ny
        return self.y
 
    def set_month(self, nm):
        self.m = str(nm)
        return str(self.m)
 
    def set_day(self, nd):
        self.d = str(nd)
        return self.d

class AmericanDate(Date):
 
    def formatAM(self):
        if len(self.get_day()) > 1 and len(self.get_month()) > 1:
            return f'{self.get_month()}.{self.get_day()}.{self.get_year()}'
        if len(self.get_day()) == 1 and len(self.get_month()) == 1:
            return f'0{self.get_month()}.0{self.get_day()}.{self.get_year()}'
        if len(self.get_day()) > 1 and len(self.get_month()) == 1:
            return f'0{self.get_month()}.{self.get_day()}.{self.get_year()}'
        if len(self.get_day()) == 1 and len(self.get_month()) > 1:
            return f'{self.get_month()}.0{self.get_day()}.{self.get_year()}'
 
 
class EuropeanDate(Date):
 
    def formatEU(self):
        if len(self.get_day()) > 1 and len(self.get_month()) > 1:
            return f'{self.get_day()}.{self.get_month()}.{self.get_year()}'
        if len(self.get_day()) == 1 and len(self.get_month()) == 1:
            return f'0{self.get_day()}.0{self.get_month()}.{self.get_year()}'
        if len(self.get_day()) > 1 and len(self.get_month()) == 1:
            return f'{self.get_day()}.0{self.get_month()}.{self.get_year()}'
        if len(self.get_day()) == 1 and len(self.get_month()) > 1:
            return f'0{self.get_day()}.{self.get_month()}.{self.get_year()}'
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())