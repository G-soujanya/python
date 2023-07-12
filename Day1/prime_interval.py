# Python program to display all the prime numbers within an interval
lower=int(input("enter the lower bound"))
upper=int(input("enter the upper bound"))
print("prime numbers between",lower,"and",upper)
for i in range(lower,upper+1):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count=count+1
    if(count==2):
        print(i)