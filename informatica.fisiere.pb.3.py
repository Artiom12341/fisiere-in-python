with open ('globulete.txt','r') as f:
    a=f.readline()
b=int(a)+3
c=(int(a)+b)-2
x=int(a)+b+c
with open ('bradut.txt','w') as f:
    f.write(str(x))