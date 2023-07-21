#program that opens a file and writes data to it.Hands exceptions that can be generated during the I/O operations.
try:
    f=open("t.txt","r")
except IOError:
    print("file not found")