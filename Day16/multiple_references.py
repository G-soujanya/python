class Mobile:
    def __init__(self,price,brand):
        self.price=price 
        self.brand=brand 
mob1=Mobile(10000,"Apple")
print("price of mobile 1",mob1.price)
mob2=mob1
mob2.price=20000 
print("price of mobile 1",mob1.price)
print("price of mobile 1",mob2.price)