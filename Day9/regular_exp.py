import re
st="python is a high level programming language"
x=re.search("high",st)
if(x):
    print("high is sub string")
print(x.start())
print(x.end())
print(re.split(" ",st))
print(re.findall("i",st))
print(re.match("python",st))
stri="python"
print(re.fullmatch("python",st))
print(re.fullmatch("python",stri))
#meta characters
import re
p="Python is a high level programming language"
x=re.findall("^python",p)
y=re.findall("e$",p)
if(x):
    print("yes string starts with python")
if(y):
    print("yes string ends with e")
g=re.findall("python|lo",p)
if(g):
    print("yes p contain python or lo")
a=re.search("p.t",p)
print(a)
print(re.findall("le*",p))
print(re.findall("le+",p))
print(re.findall("[a-g]",p))
print(re.findall("[A-Z]",p))
print(re.findall("[^A-Z]",p))
print(re.findall("le{1}",p))
print(re.findall("(hello|level)",p))
print(re.findall("\APython",p))
print(re.findall(r"\bPython",p))
print(re.findall(r"e\b",p))
p="python3 lan@"
print(re.findall("\d",p))
print(re.findall("[^0-9]",p))
print(re.findall("\s",p))
print(re.findall("\S",p))
print(re.findall("\w",p))
print(re.findall("\W",p))
print(re.findall("@\Z",p))