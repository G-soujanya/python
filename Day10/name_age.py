#program that validates name and age as entered by the user to determine whether the person can cast vote or not
class InvalidName(Exception):
    def show(self):
        print("name can not be empty")
class InvalidAge(Exception):
    def show(self):
        print("age can not be below 18")
try:
    name=str(input("enter the name"))
    age=int(input("enter the age"))
    if(len(name)==0):
        raise InvalidName 
    if(age>18):
        print("you can cast the vote")
    else:
        raise InvalidAge
except InvalidName as e:
    e.show()
except InvalidAge as e:
    e.show()