#Python program to check if the number is an Armstrong number or not
num=int(input("Enter a number"))
sum=0
temp=num
while(temp>0):
    n=temp%10
    sum=sum+n*n*n
    temp=temp//10
if(sum==num):
    print(num,"is armstrong number")
else:
    print("Given number is not a armstrong number")