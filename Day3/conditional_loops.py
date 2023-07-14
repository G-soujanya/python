#conditional_statements
#if
count=5
if(count>=5):
    print("python")
#if_else
count=-1
if(count>0):
    print("positive")
else:
    print("negative")
#elif ladder
marks=98
if(marks<=40):
    print("pass")
elif(marks<=60):
    print("average")
elif(marks<=90):
    print("good")
else:
    print("excellent")
#nested if
sum=51
if(sum>=0):
    if(sum%2==0):
        print("even")
    else:
        print("odd")
else:
    print("negative")
#looping statements
#for loop
string="python"
for i in  string:
    print(i)
l=len(string)
for i in range(l):
    print(string[i],end=" ")
print("\n")
for i in range(3,l):
    print(string[i],end=" ")
print("\n")
for i in range(0,l,2):
    print(string[i],end=" ")
print("\n")
#while
count=0
while(count<=10):
    print(count,end=' ')
    count+=1
#break and continue
c=0
while(c<10):
    print(c)
    c+=1
    if(c==5):
        print("c is equal to 5")
        break
#continue
while(c<10):
    c+=1
    if(c==8):
        continue
    print(c)
#enumerate and pass
s="abc"
for i in enumerate(s):
    print(i)
for count,i in enumerate(s):
    pass
print(count,i)
