#program which infinitely prints natural numbers.Raise the StopIteration exception after displaying first 20 numbers to exit from the program.
n=0
while True:
    try:
        n=n+1
        if(n>20):
            raise StopIteration 
        else:
            print(n,end=" ")
    except StopIteration:
        break
