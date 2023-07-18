#NotImplementedError to restrict the instantiation of class.abstract classes serves as a template for other classes by defining a list of methods that the classes must implement
class Fruit:
    def taste(self):
        raise NotImplementedError()
    def rich_in(self):
        raise NotImplementedError()
    def colour(self):
        raise NotImplementedError() 
class Mango(Fruit):
    def taste(self):
        return "sweet"
    def rich_in(self):
        return "Vitamin A"
    def colour(self):
        return "Yellow"
class Orange(Fruit):
    def taste(self):
        return "Sour"
    def rich_in(self):
        return "Vitamin C"
    def colour(self):
        return "Orange"
a=Mango()
print(a.taste(),a.rich_in(),a.colour())
b=Orange()
print(b.taste(),b.rich_in(),b.colour())
