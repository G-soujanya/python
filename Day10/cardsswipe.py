t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    curr=0
    maxm=0
    d={}
    for i in range(len(a)):
        d[a[i]]=False
    for j in range(n):
        if d[a[j]]:
            curr=curr-1 
            d[a[j]]=False
        else:
            curr=curr+1 
            d[a[j]]=True
        maxm=max(maxm,curr)
    print(maxm)
