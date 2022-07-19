class Date:
    def __init__(self, y, m, d):
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
        
        
        
dateAM = AmericanDate(2001, 1, 2)        
print(dateAM.formatAM())

dateEU = EuropeanDate(2001, 1, 2)        
print(dateEU.formatEU())
