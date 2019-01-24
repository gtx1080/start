import numpy as np
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
class Tree():
    def __init__(self,cargo,left=None,right=None):
        self.cargo=cargo
        self.left=left
        self.right=right
import numpy as np
#Q10(a)
a=Stack()#stack to be searched from
ret=Stack()
R=input("input the item you are searching for")#the string being searched for
while True:
    b=a.pop()
    if b==R:
        print(a.size())
        break
    ret.push(b)
while ret.size():
    a.push=ret.pop()
#Q12(c)
mat=np.array([[7,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,-3,0,9,0],
            [0,0,0,0,0,0],
            [0,0,-1,0,0,0],
            [0,-6,0,0,-5,1]])
values=[]
rowc=[]
col=[]
count=0
for i in range(6):
    for j in range(6):
        if mat[i][j]!=0:
            values.append(mat[i][j])
            col.append(j)
            count=count+1
    rowc.append(count)
print(values,rowc,col)
#Q10
tree=Tree()
s=Stack()
names=[]
for i in names:
    s.push(i)
while(s.size()):
    r=Tree(s.pop())
    finish = False
    cur=tree
    while not finish:
        if r.cargo >cur.cargo:
            if cur.right == None:
                cur.right=r
                finish= True
            else:
                cur=cur.right
        else:
            if cur.left == None:
                cur.left=r
                finish= True
            else:
                cur=cur.left
