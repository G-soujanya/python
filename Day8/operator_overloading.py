class Complex:
    def __init__(self):
        self.real=0
        self.img=0
    def setValues(self,real,img):
        self.real=real
        self.img=img
    def __add__(self,c):
        t=Complex()
        t.real=self.real+c.real
        t.img=self.img+c.img
        return t
    def display(self):
        print("(",self.real,"+",self.img,"i)")
c1=Complex()
c1.setValues(1,2)
c2=Complex()
c2.setValues(3,4)
c3=Complex()
c3=c1+c2
c3.display()