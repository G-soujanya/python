class Flower:
    def __init__(self):
        self.__flower_name=None 
        self.__price_per_kg=None 
        self.__stock_available=None
    def set_flower_name(self,flower_name):
        self.__flower_name=flower_name 
    def set_price_per_kg(self,price_per_kg):
        self.__price_per_kg=price_per_kg 
    def set_stock_available(self,stock_available):
        self.__stock_available=stock_available 
    def get_flower_name(self):
        return self.__flower_name 
    def get_price_per_kg(self):
        return self.__price_per_kg 
    def get_stock_available(self):
        return self.__stock_available 
    def validate_flower(self):
        self.__flower_name=self.__flower_name.lower()
        if(self.__flower_name in ["orchid","rose","jasmine"])
            return True 
        else:
            return False 
    def validate_stock(self,required_quantity):
        if(required_quantity<=self.__stock_available):
            return True 
        else:
            return False 
    def sell_flower(self):
        required_quantity=int(input())
        if(self.validate_stock(required_quantity) and self.validate_flower()):
            self.__stock_available=self.__stock_available-required_quantity 
    def check_level(self):
        self.__flower_name=self.__flower_name.lower()
        if((self.__flower_name=="orchid" and self.__stock_available<15) or (self.__flower_name=="rose" and self.__stock_available<25) or (self.__flower_name=="jasmine" and self.__stock_available<40)):
            return True 
        else:
            return False 
f=Flower()
f.set_flower_name("orchid")
f.set_price_per_kg(5)
f.set_stock_available(100)
f.sell_flower()
f.check_level()
