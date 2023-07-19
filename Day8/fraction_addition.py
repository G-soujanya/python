#program that overloads the + operator so that it can add two objects of class fraction.
def common_divisor(num,deno):
    if(deno==0):
        return num
    else:
        return common_divisor(deno,num%deno)
class Fraction:
    def __init__(self):
        self.num=0
        self.deno=0
    def getValues(self):
        self.num=int(input("enter the numerator value"))
        self.deno=int(input("entert the denominator value"))
    def simplify(self):
        cd=common_divisor(self.num,self.deno)
        self.num=self.num//cd
        self.deno=self.deno//cd
    def __add__(self,f):
        t=Fraction()
        t.num=(self.num*f.deno)+(self.deno*f.num)
        t.deno=self.deno*f.deno 
        return t 
    def display(self):
        print(self.num,"/",self.deno)
f1=Fraction()
f1.getValues()
f2=Fraction()
f2.getValues()
f3=Fraction()
f3=f1+f2
f3.simplify()
f3.display()