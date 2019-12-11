#14M6
import random
a=random.randint(0,9)
b=random.randint(0,9)
c=random.randint(1,4)
d=0
e=0
if c==1:
    d=a+b
    e=int(input("what is the whole number result for "+str(a)+'+'+str(b)+"?"))
if c==2:
    d=a*b
    e = int(input("what is the whole number result for " + str(a) + '*' + str(b) + "?"))
if c==3:
    d=a-b
    e=int(input("what is the whole number result for "+str(a)+'-'+str(b)+"?"))
if c==4:
    if b==0:
        b=random.randint(1,9)
    d=int(a/b)
    e = int(input("what is the whole number result for " + str(a) + '/' + str(b) + "?"))
if e == d:
    print("correct")
else:
    print("not correct, the answer is " + str(d))