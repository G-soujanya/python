class student:
    name="soujanya"
    id=161
    def details(self):
        print("%d hold by %s"%(self.id,self.name))
s=student()
s.details()
print(s.name)
#constructor
class stu:
    def __init__(self):
        print("abc")
f=stu()
class ABC():
    class_var=0
    def __init__(self,var):
        ABC.class_var+=1
        self.var=var    
        print("the object value is:",var)
        print("the value of class variable is:",ABC.class_var)
obj1=ABC(10)
obj2=ABC(20)
obj3=ABC(30)
class Number:
    even=0
    def check(self,num):
        if(num%2==0):
            self.even=1
    def Even_odd(self,num):
        if(self.even==1):
            print(num,"is even")
        else:
            print(num,"is odd")
n=Number()
n.check(10)
n.Even_odd(10)
class Number:
    evens=[]
    odds=[]
    def __init__(self,num):
        if(num%2==0):
            Number.evens.append(num)
        else:
            Number.odds.append(num)
n1=Number(10)
n2=Number(31)
print("even numbers are:",Number.evens)
print("odd numbers are:",Number.odds)
class ABC:
    class_var=0
    def __init__(self,var):
        ABC.class_var+=1
        self.var=var
        print("object varible value is",var)
        print("class variable value is",ABC.class_var)
    def __del__(self):
        print("object with value %d is going out of scope"%(self.var))
obj1=ABC(10)
obj2=ABC(20)
del obj1
del obj2
class ABC:
    def __init__(self,name,var):
        self.name=name
        self.var=var
    def __repr__(self):
        return repr(self.var)
    def __len__(self):
        return len(self.name)
    def __cmp__(self,obj):
        return self.var-obj.var 
obj=ABC("abcdf",10)
print("the value stored in object is",repr(obj))
print("The length of value stored in object",len(obj))
obj1=ABC("ghijk",11)
val=obj.__cmp__(obj1)
if(val==0):
    print("Both values are equal")
elif(val==-1):
    print("first value less then second")
else:
    print("second value is less than first")
class Number:
    def __init__(self,myList):
        self.myList=myList
    def __getitem__(self,index):
        return self.myList[index]
    def __setitem__(self,index,val):
        self.myList[index]=val
NumList=Number([1,2,3,4,5])
print(NumList[2])
NumList[3]=10
print(NumList.myList)
#public and private variables
class ABC:
    def __init__(self,var1,var2):
        self.var1=var1 
        self.__var2=var2
    def display(self):
        print('var1=',self.var1)
        print('var2=',self.__var2)
obj=ABC(10,20)
obj.display()
print("var1=",obj.var1)
print("var2=",obj._ABC__var2)
class ABC:
    def __init__(self,var):
        self.__var=var
    def __display(self):
        print("From class method,var=",self.__var)
obj=ABC(10)
obj._ABC__display()
#calling a class method from another class method
class ABC:
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is=",self.var)
    def add_2(self):
        self.var+=2
        self.display()
obj=ABC(10)
obj.add_2()
class ABC:
    #this is docstring
pass
print(ABC.__doc__)
# program to show how a class method calls a function defined in the global namespace
def scale_10(x):
    return x*10
class ABC:
    def __init__(self,var):
        self.var=var 
    def display(self):
        print("var is",self.var)
    def modify(self):
        self.var=scale_10(self.var)
obj=ABC(1)
obj.display()
obj.modify()
obj.display()
