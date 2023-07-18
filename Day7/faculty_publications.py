#program that has a class person.inherit a class faculty from person which also has a class publications
class Person:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def display(self):
        print("NAME :",self.name)
        print("AGE:",self.age)
        print("SEX:",self.sex)
class publications:
    def __init__(self,no_rp,no_books,no_arts):
        self.no_RP=no_rp
        self.no_Books=no_books
        self.no_Arts=no_arts
    def display(self):
        print("Number of research papers published",self.no_RP)
        print("Number of books published",self.no_Books)
        print("Number of Articles published",self.no_Arts)
class Faculty(Person):
    def __init__(self,name,age,sex,desig,dept,no_rp,no_books,no_arts):
        Person.__init__(self,name,age,sex)
        self.desig=desig
        self.dept=dept
        self.pub=publications(no_rp,no_books,no_arts)
    def display(self):
        Person.display(self)
        print("designation is",self.desig)
        print("deparment is",self.dept)
        self.pub.display()
f=Faculty("pooja",38,"Female","tic","maths",22,1,3)
f.display()