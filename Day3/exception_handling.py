try:
    print(hello)
except:
    print("variable not defined")
#
try:
    print(hello)
except Exception as e:
    print(e)
finally:
    print("always excecuted")
#
try:
    list=[10,20,30]
    print(list[9])
except IndexError as e:
    print(e)
#
try:
    f=open("a.txt")
except:
    print("file not found")
#
try:
    n=int(input())
    print(1/n)
except ValueError as v:
    print(v)
except ZeroDivisionError as z:
    print(z)
else:
    print("excecuted successfuly")
finally:
    print("finally block")
#user defined exception
class NewException(Exception):
    pass
try:
    attper=int(input("enter the attendance percentage"))
    if(attper<75):
        raise NewException
    else:
        print("you eligible to write EST")
except NewException:
    print("your attendance percentage is below 75%")
#raising exception
x=-1
if(x<0):
    raise Exception("error")
try:
    x="hello"
    if not type(x) is int:
        raise TypeError("only integers are allowed")
except TypeError as v:
    print(v)
