#lex_auth_012753087522512896330
#Start writing your code here
#lex_auth_012753087522512896330
#Start writing your code here
class Apparel:
    counter=100 
    def __init__(self,price,item_type):
        self.__price=price 
        self.__item_type=item_type 
        Apparel.counter+=1 
        self.__item_id=self.__item_type[0]+str(Apparel.counter) 
    def get_item_id(self):
        return self.__item_id 
    def get_price(self):
        return self.__price 
    def get_item_type(self):
        return self.__item_type 
    def set_price(self,price):
        self.__price=price 
    def calculate_price(self):
        self.__price+=self.__price*5/100
class Cotton(Apparel):
    def __init__(self,price,discount):
        super().__init__(price,"Cotton")
        self.__discount=discount 
    def get_discount(self):
        return self.__discount 
    def calculate_price(self):
        super().calculate_price()
        price=self.get_price() 
        price-=price*self.__discount/100 
        price+=price*5/100 
        self.set_price(price)
class Silk(Apparel):
    def __init__(self,price):
        super().__init__(price,"Silk")
        self.__points=None
    def calculate_price(self):
        super().calculate_price()
        if(self.get_price()>10000):
            self.__points=10 
        else:
            self.__points=3
        self.set_price(self.get_price()+self.get_price()*10/100)
    def get_points(self):
        return self.__points
c=Cotton(100,10)
s=Silk(100)
c.calcualte_price()
s.calcualte_price()
print(c.get_discount)
print(s.get_points)        