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

astr='()()((((())))(()((()'
b=stack()
for i in astr:
    if i=='(':
        b.push('(')
    else:
        b.pop()
print(len(b.read()))