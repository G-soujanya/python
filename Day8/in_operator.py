#program to override the in operator
class Marks:
    def __init__(self):
        self.marks={"maths":100,"computers":50,"sst":100,"science":76}
    def __contains__(self,subject):
        if subject in self.marks:
            return True
        else:
            return False
    def __getitem__(self,sub):
        return self.marks[sub]
m=Marks()
s=str(input("enter the subject"))
if s in m:
    print("weightage",m[s])