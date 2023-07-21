class ValueTooLarge(Exception):
    def show(self):
        print("value is too large")
class ValueTooSmall(Exception):
    def show(self):
        print("value is too smalll")
max=100
try:
    n=int(input("enter a number"))
    if(n==max):
        print("valid number")
    elif(n>max):
        raise ValueTooLarge 
    else:
        raise ValueTooSmall 
except ValueTooLarge as e:
    e.show()
except ValueTooSmall as e:
    e.show()