#program that overloads the + operator on a class student that has attributes name and marks
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(self.name,self.marks)
    def __add__(self,s):
        t=Student(s.name,[])
        for i in range(len(self.marks)):
            t.marks.append(self.marks[i]+s.marks[i])
        return t 
s1=Student("nikhil",[87,90,85])
s2=Student("nikhil",[83,86,88])
s1.display()
s2.display()
s3=Student("h",[])
s3=s1+s2
s3.display()
