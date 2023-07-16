#built in functions to check,get,set,and delete class attribute
class ABC:
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var value is",self.var)
obj=ABC(10)
obj.display()
print("check whethere object has var attribute or not",hasattr(obj,'var'))
getattr(obj,'var')
setattr(obj,'var',50)
print("After updation var value is",obj.var)
setattr(obj,'count',110)
print("New attribute count value is",obj.count)
delattr(obj,'var')
#built class attribute
class ABC:
    '''class attribute'''
    def __init__(self,var1,var2):
        self.var1=var1
        self.var2=var2
    def display(self):
        print("var1 value is",self.var1)
        print("var2 value is",self.var2)
obj=ABC(10,20)
print("object.__dict___",obj.__dict__)
print("object.__doc__",obj.__doc__)
print("class.__name__",ABC.__name__)
print("object.__module___",obj.__module__)
print("class.__bases___",ABC.__bases__)
#class methods
class Rectangle:
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
    @classmethod
    def square(cls,side):
        return cls(side,side)
obj=Rectangle.square(5)
print("Area is",obj.area())
#static methods
#static methods are bound to class,no need of creation of object
class cal:
    @staticmethod
    def add(x,y):
        return x+y
print("addition is",cal.add(1,2))
