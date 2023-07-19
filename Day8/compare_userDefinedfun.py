#program to compare two objects of user-defined class type
class Book:
    def __init__(self):
        title=""
        publisher=""
        price=0
    def set(self,title,publisher,price):
        self.title=title
        self.publisher=publisher
        self.price=price
    def display(self):
        print("TITLE :",self.title)
        print("PUBLISHER:",self.publisher)
        print("PRICE",self.price)
    def __gt__(self,b):
        if(self.price>b.price):
            return True
        else:
            return False
b1=Book()
b1.set("OOP","oxford",525)
b2=Book()
b2.set("Let","BPB",300)
if(b1>b2):
    print("this book has morw knowledge so i will buy")
    b1.display()