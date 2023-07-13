#accessing and slicing
list=[10,1.5,"python"]
print(list[1])
print(list[-1])
print(list[:2])
print(list[1:])
print(list[::2])
print(list[::-1])
#methods
list.append(9)
print(list)
list.insert(1,11)
print(list)
list.pop()
print(list)
list.pop(0)
print(list)
l=[9,2,3,4]
l.sort()
print(l)
l1=[6,5,2,3]
l1.clear()#remove all elements
print(l1)
strh="h e l l o"
print(strh.split())#convert into list
#display a state names  which starts with a
list=['andhra pradhesh','arunachal pradhesh','bihar',"sikkim"]
for i in list:
    if(i.startswith("a")):
        print(i)
