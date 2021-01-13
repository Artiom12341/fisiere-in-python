with open ('numar.txt','r') as f:
    a=f.readline()
a1=int(a)*1
a2=int(a)*2
a3=int(a)*3
a4=int(a)*4
a5=int(a)*5
a6=int(a)*6
a7=int(a)*7
a8=int(a)*8
a9=int(a)*9
a10=int(a)*10
with open ('inmultire.txt','w') as f:
    f.write('1*'+a+'='+str(a1))
    f.write(' ')
    f.write('2*'+a+'='+str(a2))
    f.write(' ')
    f.write('3*'+a+'='+str(a3))
    f.write(' ')
    f.write('4*'+a+'='+str(a4))
    f.write(' ')
    f.write('5*'+a+'='+str(a5))
    f.write(' ')
    f.write('6*'+a+'='+str(a6))
    f.write(' ')
    f.write('7*'+a+'='+str(a7))
    f.write(' ')
    f.write('8*'+a+'='+str(a8))
    f.write(' ')
    f.write('9*'+a+'='+str(a9))
    f.write(' ')
    f.write('10*'+a+'='+str(a10))
    f.write(' ')