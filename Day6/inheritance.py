class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age 
    def display(self):
        print("NAME:",self.name)
        print("AGE:",self.age)
class Teacher(Person):
    def __init__(self,name,age,exp,r_area):
        Person.__init__(self,name,age)
        self.exp=exp
        self.r_area=r_area
    def displayData(self):
        Person.display(self)
        print("EXPERIENCE:",self.exp)
        print("RESEARCH AREA:",self.r_area)
class Student(Person):
    def __init__(self,name,age,course,marks):
        Person.__init__(self,name,age)
        self.course=course
        self.marks=marks
    def displayData(self):
        Person.display(self)
        print("COURSE:",self.course)
        print("MARKS:",self.marks)
print("**********TEACHER************")
t=Teacher("jaya",43,20,"Recommender System")
t.displayData()
print("*************STUDENT*********")
s=Student("manu",20,"Btech",78)
s.displayData()
#isinstance() and is subclass() used to return true if the object is an instance of the class or other classes derived from it, issubclass checks for inheritance
print("T is teacher",isinstance(t,Teacher))
print("T is person",isinstance(t,Person))
print("T is an integer",isinstance(t,int))
print("T is an object",isinstance(t,object))#by default every class inherits from object class
print("person is a subclass of teacher:",issubclass(Person,Teacher))
print("teacher is a subclass of person:",issubclass(Teacher,Person))
print("Boolean is a subclass of int",issubclass(bool,int))