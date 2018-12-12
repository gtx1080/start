import numpy as np
import random
a=np.zeros((10,10))
for i in range(10):
    for j in range(10):
        a[i][j]=random.randint(0,2)
deter=False
print("original:")
print(a)
count=1
while deter==False:
    ac=0
    node0=[]
    node1=[]
    for i in range(10):
        for j in range(10):
            now=a[i][j]
            if now==2:
                continue
            jud=0
            tot=0
            if(i>0):
                tot=tot+1
                if now!=2:
                    jud=jud+a[i-1][j]
            if(j>0):
                tot=tot + 1
                if now != 2:
                    jud = jud + a[i][j-1]
            if(i<9):
                tot=tot+1
                if now != 2:
                    jud=jud+a[i+1][j]
            if(j<9):
                tot=tot+1
                if now != 2:
                    jud=jud+a[i][j+1]
            if(i>0 and j>0):
                tot=tot+1
                if now != 2:
                    jud=jud+a[i-1][j-1]
            if(i>0 and j<9):
                tot=tot+1
                if now != 2:
                    jud=jud+a[i-1][j+1]
            if(i<9 and j>0):
                tot=tot+1
                if now != 2:
                    jud=jud+a[i+1][j-1]
            if(i<9 and j<9):
                tot=tot+1
                if now != 2:
                    jud=jud+a[i+1][j+1]
            if(((jud/tot)>0.5 and now==1) or ((jud/tot)<0.5 and now==0)):
                ac=ac+1
            else:
                if(now==0):
                    node0.append([i,j])
                    if(len(node1)):
                        st=node1[-1]
                        a[st[0],st[1]],a[i][j]=a[i][j],a[st[0],st[1]]
                        node0.pop()
                        node1.pop()
                else:
                    node1.append([i,j])
                    if (len(node0)):
                        st = node0[-1]
                        a[st[0], st[1]], a[i][j] = a[i][j], a[st[0], st[1]]
                        node0.pop()
                        node1.pop()
    print('attempt '+str(count))
    print(a)
    count=count+1
    if(ac>90):
        deter=True