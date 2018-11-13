class stack():
    def __init__(self):
        self.stack1=[]
    def isempty(self):
        if len(self.stack1)==0:
            return True
        else:
            return len(self.stack1)
    def push(self,a):
        self.stack1.append(a)
    def pop(self):
        a=self.stack1[len(self.stack1)-1]
        self.stack1.remove(self.stack1[len(self.stack1)-1])
        return a
    def read(self):
        return self.stack1

astr='(())()()'
b=stack()
over=False
for i in astr:
    if i=='(':
        b.push('(')
    elif(len(b.read())>0):
        b.pop()
    else:
        over=True
        break
if len(b.read())!=0 or over:
    print(False)
else:
    print(True)
a=stack()
b=[1,2,3,4,5]
c=[]
for i in b:
    a.push(i)
for i in range(len(b)):
    c.append(a.pop())
print(c)
