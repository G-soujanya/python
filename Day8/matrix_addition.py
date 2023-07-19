#program that overloads the + operator to add two objects of class matrix
class Matrix:
    def __init__(self,list):
        self.list=list
    def display(self):
        print(self.list)
    def __add__(self,m):
        t=Matrix([])
        for i in range(len(self.list)):
            for j in range(len(self.list[i])):
                t.list.append(self.list[i][j]+m.list[i][j])
        return t 
m1=Matrix([[1,2],[3,4]])
m2=Matrix([[3,4],[5,1]])
m3=Matrix([])
m3=m1+m2 
m3.display()