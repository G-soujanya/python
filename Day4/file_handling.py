#opening file and reading a file
f=open("file.txt","r")
print(f.read())
f.close()
f=open("file.txt","r")
print(f.readline())
print(f.readline())
f=open("file.txt","r")
print(f.readlines())
print(f.read(10))
f=open("file.txt","r")
for i in f:
    print(i)
#writing into file
f=open("file1.txt","w")
f.write("congrations")
f.close()
f=open("file1.txt","w")
f.writelines(["1\n","2"])
f.close()
f=open("file1.txt","a")
f.writelines(["3\n","4"])
f.close()
with open("file1.txt","r") as fp:
    data=fp.readlines()
    for i in data:
        words=i.split()
        print(words)