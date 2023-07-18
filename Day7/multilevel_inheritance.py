#linearization of class:any specified attribute is first searched in the current class next parent next grand parent
#method resolution order(MRO):set of rules to find this linearization
#MRO of can be checked by using mro() return list,__mro__ return tuple
 #base class
class Person:            
    def name(self):
        print("Name...")
#class derived form Person
class Teacher(Person): 
    def qualification(self):
        print("ph.D must")
#class derived from Teacher,now hierarchy is person->teacher->HOD
class HOD(Teacher):
    def exp(self):
        print("15 years")
hod=HOD()
hod.name()
hod.qualification()
hod.exp()