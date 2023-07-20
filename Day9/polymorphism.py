#____duck typing______
class pychart:
    def execute(self):
        print("running")
class laptop:
    def code(self,ide):
        ide.execute()
class myeditors():
    def execute(self):
        print("running")
        print("compailing")
ide=myeditors()
idle=pychart()
lap1=laptop()
print("*********")
lap1.code(ide)
print("*********")
lap1.code(idle)
class Dog:
    def make_Sound(self):
        return "woof"
class Duck:
    def make_Sound(self):
        return "quack"
class animal:
    def make_sound_of_animal(self,animal):
        return animal.make_Sound()
d=Dog()
duck=Duck()
a=animal()
print(a.make_sound_of_animal(d))
print(a.make_sound_of_animal(duck))
#___________method overloading_____
class student:
    def __init__(self):
        self.m1=0
        self.m2=0
    def sum(self,a=None,b=None,c=None):
        if(a!=None and b!=None and c!=None):
            print(a+b+c)
        elif(a!=None and b!=None):
            print(a+b)
s=student()
s.sum(1,2)
s.sum(1,2,3)
#___________method overriding__________
class student:
    def show(self):
        print("This is student classs")
class person(student):
    def show(self):
        super().show()
        print("This is person class")
s=person()
s.show()
#__operator overloading_____