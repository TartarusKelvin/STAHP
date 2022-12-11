from operators import ops
from stack import op
from GLOBAL import *

def readtoken(t):
    if t[0]=="`":
        df=t.count('`')
        t=t[df:]
        if t in ops:
            STACK.add(op(ops[t],t,df=df))
            return
    if t in ops:
        STACK.add(op(ops[t],t))
        return
    try:
        STACK.add(int(t))
    except:
        if t.isupper():
            STACK.add(t.lower())
            STACK.add(op(ops["<"],"<"))
            STACK.add(op(ops["¬"],"¬"))
            return
        STACK.add(t)

def loadfile(fpath):
    with open(fpath,"r") as f:
        for line in f:
            tokens=line.strip().split(" ")[::-1]
            for t in tokens:
                readtoken(t)
            STACK.kill()
loadfile("std.stahp")
while True:
    line=input("stahp) ")
    tokens = line.strip().split(" ")[::-1]
    for t in tokens:
        readtoken(t)
    if STACK.count()>0:
        print(STACK.peak())
    STACK.kill()
