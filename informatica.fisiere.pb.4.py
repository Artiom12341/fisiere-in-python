with open ('input.txt','r') as f:
    a=f.readline()
b=int(a)-2
c=int(a)-1
d=int(a)+1
e=int(a)+2
x=' '
with open('output.txt','w') as f:
    f.write(str(b)+str(x)+str(c)+str(x)+str(a)+str(x)+str(d)+str(x)+str(e))