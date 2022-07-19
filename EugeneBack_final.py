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