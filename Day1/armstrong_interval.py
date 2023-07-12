# Program to check Armstrong numbers in a certain interval
lower=int(input("enter the lower range"))
upper=int(input("enter the upper range"))
for i in range(lower,upper+1):
    sum=0
    temp=i
    order=len(str(i))
    while(temp>0): 
        n=temp%10
        sum=sum+n**order
        temp=temp//10
    if(sum==i):
        print(i)
    
