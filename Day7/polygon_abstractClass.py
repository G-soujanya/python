#program that has an abstract class polygon.Derive two classes Rectangle and Triangle from polygon and triangle from polygon and write methods to get the details of their dimension and hence calcualte the area
class Polygon:
    def get_data(self):
        raise NotImplementedError()
    def area(self):
        raise NotImplementedError()
class Triangle(Polygon):
    def get_data(self):
        self.base=float(input("enter the length"))
        self.height=float(input("enter the breadth"))
    def area(self):
        print("Triangle area is",((1/2)*self.base*self.height))
class Rectangle(Polygon):
    def get_data(self):
        self.length=float(input("enter the length"))
        self.breadth=float(input("enter the breadth"))
    def area(self):
        print("Rectangle area is",self.length*self.breadth)
t=Triangle()
t.get_data()
t.area()
r=Rectangle()
r.get_data()
r.area()