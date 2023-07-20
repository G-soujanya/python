#private variable
class abc():
    def __init__(self,var1,var2):
        self.var1=var1
        self.__var2=var2
    def display(self):
        print("var1=",self.var1)
        print("var2=",self.__var2)
class a(abc):
    def show(self):
        print(self.__var2)
h=a(1,2)
h.show()
obj=abc(10,20)
obj.display()
#private method
#print("var2=",obj._abc__var2)
class ABC:
    def __init__(self,var):
        self.var=var
    def __display(self):
        print("var",self.var)
ob=ABC(10)
ob._ABC__display()