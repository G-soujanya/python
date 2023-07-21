#program that prompt the user to enter a number.if the number is positive or zero print it,otherwise raise an expression.
try:
    n=int(input("enter a number"))
    if(n>=0):
        print(n)
    else:
        raise ValueError("negative value")
except ValueError as e:
    print(e)