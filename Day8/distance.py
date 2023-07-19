#program to oveerload -= oprator to subtract two distance
class Distance:
    def __init__(self):
        self.km=0
        self.m=0
    def set(self,km,m):
        self.km=km
        self.m=m
    def __isub__(self,d):
        self.m=self.m-d.m
        if(self.m<0):
            self.m+=1000
            self.km-=1
        self.km=self.km-d.km
        return self
    def display(self):
        print(self.km,"kms",self.m,"ms")
d1=Distance()
d1.set(21,70)
d2=Distance()
d2.set(18,123)
d1-=d2
d1.display()
