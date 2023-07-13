set={10,100,30,20}
print(set)
print(sorted(set))
print(sum(set))
#comparision
s1={10,30,20,90}
s2={40,60,50,90}
print(s1.union(s2))
print(s1|s2)
print(s1.intersection(s2))
print(s1&s2)
print(s1.difference(s2))
print(s1-s2)
a={10,20,30}
b={40}
b=a#changes reflected in b also
print(a,b)
a.add(50)
print(a,b)
c={10,20,30}
d={40}
d=c.copy()#changes not reflected in d
print(a,b)
c.add(50)
print(c,d)