import numpy as np
def teardown(strr):
    a=[]
    for i in strr:
        if isinstance(i,list) or isinstance(i,str):
            a.append(teardown(i))
        elif i !='[' and i!=']' and ord(i)!=92:
            a.append(i)
        print(a)
        return a
class stack:
    def __init__(self):
        self.stack1=[]
    def isempty(self):
        if len(self.stack1)==0:
            return True
        else:
            return False
    def push(self,a):
        self.stack1.append(a)
    def pop(self):
        # a=self.stack1[len(self.stack1)-1]
        # del self.stack1[len(self.stack1)-1]
        return self.stack1.pop()
    def read(self):
        return self.stack1
A='10 2 8 * + 3 -'
start=0
A=A.split(" ")
op=['+','-','*','/']
'''
for i in range(len(instr)):
    if instr[i]==' ' and instr[i-1] not in op:
        A.append(eval(instr[start:i]))
        start=i
    elif instr[i]==' ' and instr[i-1] in op:
        A.append(instr[i-1])
        start=i
'''
R=stack()
for i in A:
    if i not in op:
        R.push(i)
    else:
        x=str(R.pop())
        y=str(R.pop())
        R.push(eval(y+i+x))
print(R.read())
P=stack()
for i in A:
    if i not in op:
        P.push(i)
    else:
        y=str(P.pop())
        x=str(P.pop())
        #P.push('(')
        #P.push(x)
        #P.push(i)
        #P.push(y)
        #P.push(')')
        s = ""
        for j in ['(',x,i,y,')']: # here important
            s += j
        P.push(s)
    print(P.read())

a = str(P.read())
# a=str(list(np.array(a).flatten()))
b=[]
# print(a)
for i in a:
    if (i!='[' and i!=']' and ord(i)!=92):
        b.append(i)
for i in b:
    if i!=',':
        print(i,end='')