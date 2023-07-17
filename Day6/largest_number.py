#program that has a class Number with values stored in list.Write a class method to find largest value.
class Number:
    def __init__(self):
        self.values=[]
    def find_max(self):
        max=''
        for i in self.values:
            if(i>max):
                max=i 
        print("maximum value is %r",max)
    def insert_values(self):
        value=input("enter value..")
        self.values.append(value)
s=Number()
ch='y'
while(ch=='y'):
    s.insert_values()
    ch=input('do you want to enter more values press y')
s.find_max()