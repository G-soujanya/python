def add(a,b):
    print("addition of {} and {} is {}".format(a,b,a+b))
add(2,3)
#categories of functions
#without arguments and without return values
def info():
    print("hello")
info()
#without arguments and with return values
def day():
    return "friday"
print(day())
#with arguments and with return values
def sub(x,y):
    return x-y
print(sub(90,10))
#with arguments and without return values
def div(x,y):
    print(x/y)
div(14,7)
#with arguments and without values
def g(id,name="nithya"):
    print("%d hold by %s"%(id,name))
g(161,"nithya")
"""
def g(name="nithya",id):
    print("%d hold by %s"%(id,name))
g("nithya",161)
"""
#*args
def sumn(*args):
    sum=0
    for i in args:
        sum+=i 
    print(sum)
sumn(1,2,3)
sumn(1,2,3,4,5)
#**kwargs
def go(**kargs):
    print("name is {}".format(kargs['name']))
    print(kargs,type(kargs))
go(name="abc")
def h(**weekdays):
    for i in weekdays.values():
        print(i)
h(day1="monday",day2="tuesday",day3="wednesday",day4="thursday",day5="friday",day6="saturaday")
#anonymous functions
sum=lambda a,b:print(a+b)
sum(9,10)
#recursive functions
def add(a):
    if(a==0):
        return 0
    return a+add(a-1)
print(add(4))
#__doc__
def add(a,b):
    "this method return addition of two numbers"
    return a+b
print(add(1,2))
print(add.__doc__)
import math
print(math.sqrt(16))
print(math.sqrt.__doc__)