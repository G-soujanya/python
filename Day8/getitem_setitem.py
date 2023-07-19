#program overrides __getitem__() and __setitem__() methods in class
class List:
    def __init__(self,list):
        self.list=list
    def __getitem__(self,index):
        return self.list[index]
    def __setitem__(self,index,value):
        self.list[index]=value
    def __len__(self):
        return len(self.list)
    def display(self):
        print(self.list)
l=List([1,2,3,4,5,6,7])
print("LIST IS:")
l.display()
index=int(input("enter the index"))
print(l[index])
index=int(input("enter the index"))
value=int(input("enter the value"))
l[index]=value
l.display()
print("Length of list is:",len(l))
