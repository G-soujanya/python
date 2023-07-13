#immutable
#accessing and slicing
s="python is a programmimg language"
print(s[2])#print value at that index
print(s[-1])#print last character
print(s[:8])#print entire string upto specified index
print(s[8:])#print entire string from specified index
print(s[:-1])#print entire string except last character
print(s[::2])#print entire string with step two
print(s[::-1])#print string in reverse order
print(s[6:0:-1])
#methods
st="PYTHON programmimg"
print(st.lower())
print(st.upper())
print(len(st))
print(st+"day")#concatenating with +
print(st,"day")#concatenating with ,
print("{}{}today".format(st,"day"))#concatenating with formate method
print("%s %s today"%(st,"day"))
print(s[1].isalpha())#checking alphabet or not
print(s.isdigit())
strin="12"
print(strin[1].isalpha())
print(strin.isdigit())#checking digit or not
stri="12#"
print(stri.isalnum())#checking whether string contain only alphabets and numbers
name="       sindhu        "
print(name)
print(len(name.strip()))
print(len(name.lstrip()))
print(name.rstrip())
clg="rgukt rk"
print("#".join(clg.split()))
