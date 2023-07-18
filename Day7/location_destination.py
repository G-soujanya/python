#program that has class point.define another class location which has two objects(Location and Destination)of class point.Also define a function in location that prints the reflection of destination on the x-axis
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def get(self):
        return (self.x,self.y)
class Location:
    def __init__(self,x1,y1,x2,y2):
        self.source=Point(x1,y1)
        self.destination=Point(x2,y2)
    def show(self):
        print("Source =",self.source.get())
        print("Destination=",self.destination.get())
    def reflection(self):
        self.destination.x=-self.destination.x 
        print("Reflextion of point x axis is",self.destination.x,self.destination.y)
l=Location(1,2,3,4)
l.show()
l.reflection() 