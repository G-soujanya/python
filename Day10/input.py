num=int(input("enter the numerator"))
deno=int(input("enter the denominator"))
try:
    q=num/deno
    print("quotient is",q)
except ZeroDivisionError:
    print("denominator can not be 0")