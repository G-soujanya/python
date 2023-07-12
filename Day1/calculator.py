#Simple Calculator by Using Functions
def add(x,y):
    print("addition of two numbers is",x+y)
def sub(x,y):
    print("addition of two numbers is",x-y)
def mul(x,y):
    print("addition of two numbers is",x*y)
def div(x,y):
    print("addition of two numbers is",x/y)
print("enter 1 for addition,2 for subtraction,3 for multiplication,4 for division")
num=int(input("enter number 1"))
num1=int(input("enter number 2"))
c=int(input("enter your choice"))
if(c==1):
    add(num,num1)
elif(c==2):
    sub(num,num1)
elif(c==3):
    mul(num,num1)
elif(c==4):
    div(num,num1)
else:
    print("invalid choice")
    