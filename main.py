from operators import ops
from stack import op
from GLOBAL import *



def readtoken(t):
    if t[0]=="`":
        df=t.count('`')
        t=t[df:]
        if t in ops:
            STACK.add(op(ops[t],df=df))
            return
    if t in ops:
        STACK.add(op(ops[t]))
        return
    try:
        STACK.add(int(t))
    except:
        STACK.add(t)

while True:
    line=input("stahp) ")
    tokens = line.strip().split(" ")[::-1]
    for t in tokens:
        readtoken(t)
    if STACK.count()>0:
        print(STACK.peak())
    STACK.kill()