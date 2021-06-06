#-*- coding = utf-8 -*-
#@Author:Catchen
#@Time:2021/3/18 下午3:20
#@File:demo1.py
#@Software:PyCharm

file = open("test.txt","r")

a=file.readline()
# b=file.readline(100)
# if b[len(b)-1]=='\n':
#     print(b)
# else:
#     c=file.readline(100)
#     print("%s%s"%(b,c))
print(a,end='')
d=file.readline()
print(d)

'''
a=file.readlines()
print(a[0])
print(a[0],a[1],sep='')
'''

'''
i=0
while i<9:
    i=i+1
    j=0
    while j<10:
        j=j+1
        print(j,"*",i,"=",i*j,sep='',end='')
        if j<i:
            print(",",sep='',end='')
        else:
            print("\n",sep='',end='')
            break
'''

'''
x=0
while x<9:
    x=x+1
    y=0
    str1=''
    while y<10:
        y=y+1
        if y<=x:
            if y==1:
                str1=str(y)+"*"+str(x)+"="+str(x*y)
            else:
                str1=str1+","+str(y)+"*"+str(x)+"="+str(x*y)
        else:
            print(str1)
            break
'''
'''
x=0
while x<9:
    x=x+1
    y=0
    str1=''
    while y<10:
        y=y+1
        str1 = str1 + str(y) + "*" + str(x) + "=" + str(x * y)
        if y<x:
            str1=str1+","
        else:
            print(str1)
            break
'''



