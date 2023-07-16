#program that has a class fraction with attributes numerator and denominator.Enter the values of the attributes and print the fraction in simplified fraction
class fraction:
    def __init__(self):
        self.numerator=int(input("enter the numerator"))
        self.denominator=int(input("enter the denominator"))
        if(self.denominator==0):
            print("fraction not possible")
            exit()
    def display(self):
        self.simplify()
        print("simplified fraction is",self.numerator,"/",self.denominator)
    def simplify(self):
        common_divisor=self.gcd(self.numerator,self.denominator)
        self.numerator=self.numerator/common_divisor
        self.denominator=self.denominator/common_divisor
    def gcd(self,a,b):
        if(b==0):
            return a 
        else:
            return self.gcd(b,a%b)
obj=fraction()
obj.display()