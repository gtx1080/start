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
a=1179087#十进制
res=stack()
b=[]
n=20
lis=[0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
while a:
    res.push(a%n)
    a=a//n
while not res.isempty():
    r=res.pop()
    if r<10:
        b.append(r)
    else:
        b.append(chr(r+55))
print(b)
