#base class | grand parent class is called indirect class
#the derived class inherite the features of the base class via two separate paths
class Student:
    def name(self):
        print("Name...")
class academic(Student):
    def acad_score(self):
        print("Academic score..90 above")
class ECA(Student):
    def eca_score(self):
        print("ECA score...60 above")
class Result(academic,ECA):
    def eligibility(self):
        print("***************MINIMUM ELIGIBILITY******")
        self.acad_score()
        self.eca_score()
r=Result()
r.eligibility()