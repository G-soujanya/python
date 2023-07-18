#also called as containership represents has a relationship
class One:
    def set(self,var):
        self.var=var
    def get(self):
        return self.var 
class Two:
    def __init__(self,var):
        self.o=One()#object of one created
    #method of class one is invoked using its object in class two
        self.o.set(var)
    def show(self):
        print("Number=",self.o.get())
t=Two(100)
t.show()
    