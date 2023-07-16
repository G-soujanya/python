#program with class employee that keeps a track of the number of employee in an organization and also stores their name,designation,and salary details.
class employee:
    emp_count=0
    def __init__(self,name,designation,salary):
        self.name=name
        self.designation=designation
        self.salary=salary
        employee.emp_count+=1
    def displayCount(self):
        print("number of employee are",employee.emp_count)
    def displayDetails(self):
        print("employe details are name",self.name,"designation",self.designation,"salary",self.salary)
obj=employee("abc","p1","1000")
obj.displayCount()
obj.displayDetails()
obj1=employee("xyz","p2","100000")
obj1.displayCount()
obj1.displayDetails()