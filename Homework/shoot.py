class stack():
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
        a=self.stack1[len(self.stack1)-1]
        del self.stack1[len(self.stack1)-1]
        return a
    def read(self):
        return self.stack1
str1='22A'#初始值
start=1
jz=16#初始值是几进制
res0=stack()
a=0
num=['0','1','2','3','4','5','6','7','8','9']
for i in range(len(str1)-1,-1,-1):
    if (str1[i]) in num:
        a=a+int(str1[i])*start
    else:
        a=a+(ord(str1[i])-55)*start
    start=start*jz
res=stack()
print(a)
b=[]
n=16#转到几进制
while a:
    res.push(a%n)
    a=a//n
while not res.isempty():
    r=res.pop()
    if r<10:
        b.append(r)
    else:
        b.append(chr(r+55))
for i in b:
    print(str(i),end='')