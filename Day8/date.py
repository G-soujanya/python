#program to compare two date objects
class Date:
    def __init__(self):
        self.d=0
        self.m=0
        self.y=0
    def get(self):
        self.d=int(input("enter the day"))
        self.m=int(input("enter the month"))
        self.y=int(input("enter the year"))
    def __eq__(self,da):
        Flag=False
        if(self.d==da.d):
            if(self.m==da.m):
                if(self.y==da.y):
                    Flag=True
        return Flag
    def __lt__(self,daa):
        Flag=False
        if(self.y<daa.y):
            if(self.m<daa.m):
                if(self.d<daa.m):
                    Flag=True
        return Flag
d1=Date()
d1.get()
d2=Date()
d2.get()
print("d1==d2",d1==d2)
print("d1<d2",d1<d2)