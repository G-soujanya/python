class Parrot:
    counter=7001
    def __init__(self,name,color):
        self.__name=name
        self.__color=color 
        self.__unique_number=Parrot.counter 
        Parrot.counter+=1 
    def set_name(self,name):
        self.__name=name 
    def set_color(self,color):
        self.__color=color 
    def set_unique_number(self):
        self.__unique_number=Parrot.counter 
    def get_name(self):
        return self.__name 
    def get_color(self):
        return self.__color 
    def get_unique_number(self):
        return self.__unique_number
p=Parrot("p","red")
p.set_name("p")
p.set_color("red")
print(p.get_name())
print(p.get_color())
print(p.get_unique_number())    