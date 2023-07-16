#program that has a class student that stores roll number,name and marks(in three subjects) of the students.Display the information(roll number,name,total marks) stored about the student
class student:
    __marks=[]
    def __init__(self,rollno,name,m1,m2,m3):
        self.rollno=rollno
        self.name=name
        student.__marks.append(m1)
        student.__marks.append(m2)
        student.__marks.append(m3)
    def display(self):
        print("name is",self.name)
        print("Roll no is",self.rollno)
        print("Total marks are",self.total())
    def total(self):
        m=student.__marks
        return m[0]+m[1]+m[2]
m1=int(input("enter the marks in subject 1"))
m2=int(input("enter the marks in subject 2"))
m3=int(input("enter the marks in subject 3"))
obj=student("161","bc",m1,m2,m3)
obj.display()