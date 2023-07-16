#program that has a class circle.use a class variable to define the value of constant PI.Use this class variable to calculate area and circumference of a circle with specified radius
class Circle:
    PI=3.14159
    def __init__(self,radius):
        self.radius=radius
    def area_circum(self):
        print("area of circle is",Circle.PI*self.radius**2)
        print("circumference of a circle is",2*Circle.PI*self.radius)
s=Circle(7.5)
s.area_circum()