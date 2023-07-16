#program that uses class to store the name and marks of student.use list to store the marks in three subjects
class student:
    def __init__(self,name):
        self.name=name
        self.marks=[]
    def entermarks(self):
        for i in range(3):
            m=int(input("enter the marks of %s in subject %d"%(self.name,i+1)))
            self.marks.append(m)
    def display(self):
        print(self.name,"got",self.marks)
obj=student("nithya")
obj.entermarks()
obj.display()