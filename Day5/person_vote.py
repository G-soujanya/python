#program that has a class person stroing name and date of birth of person.the program should subtract the dob from today's date to find out whether a person is eligible to vote or not
import datetime
class Person:
    def __init__(self,name,dob):
        self.name=name
        self.dob=dob
    def check(self):
        date=datetime.date.today()
        age=date.year-self.dob.year
        if(date<datetime.date(date.year,self.dob.month,self.dob.day)):
            age-=1
        if(age>=18):
            print(self.name,"eligible to vote")
        else:
            print(self.name,"not eligible to vote")
obj=Person("suguna",datetime.date(2010,5,28))
obj.check()