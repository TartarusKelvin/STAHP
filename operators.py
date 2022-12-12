from GLOBAL import HEAP
from stack import stack,op

def nop(s):
    pass

def prh(s):
    print(s[-1])

def prs(s):
    print(s.stack()[::-1])

def stp(s):
    exit(1)

def add(s):
    s.add(s.pop()+s.pop())

def mul(s):
    s.add(s.pop()*s.pop())

def div(s):
    s.add(s.pop()/s.pop())

def lss(s):
    s.add(min([s.pop(),s.pop()]))

def grt(s):
    s.add(max([s.pop(),s.pop()]))

def drp(s):
    s.pop()

def toh(s):
    if len(s.locale)== 0:
        HEAP[s.pop()]=s.stack()
    else:
        s.locale[-1][s.pop()]=s.stack()
    s.kill()

def frh(s):
    if len(s.locale) == 0:
        s.add(HEAP[s.pop()],extend=True)
        return
    h=s.pop()
    if isinstance(h,str) and h[0]==".":
        s.add(HEAP[h[1:]],extend=True)
        return
    s.add(s.locale[-1][h],extend=True)
    

def grv(s):
    # replay stack removing a single layer of deffered
    a=s.stack()
    s.kill()
    for x in a:
        if isinstance(x,op):
            s.add(op(x.func,x.token,df=max(x.df-1,0)))
            continue
        s.add(x)

def ech(s):
    bx=s.pop()
    out=[]
    a=s.stack()
    for x in a:
        ss=stack()
        ss.add(x)
        ss.add(bx)
        ss.add(op(frh,"<"))
        ss.add(op(grv,"¬"))
        out.extend(ss.stack())
    s.kill()
    s.add(out,extend=True)

def scn(s):
    bx=s.pop()
    a=s.stack()
    s.kill()
    s.add(a.pop(0))
    if isinstance(bx,op):
        contents=[bx]
    else:
        contents=HEAP[bx]
    out=[]
    for x in a:
        out.append(x)
        out.extend(contents)
    s.add(out,extend=True)
    s.add(op(grv,"¬"))

def upck(s):
    e=s.pop()
    s.add(e,extend=isinstance(e,list))

def pck(s):
    a=s.stack()
    s.kill()
    s.add(a)

def til(s):
    s.add(list(range(s.pop())))


def read(s):
    file=s.pop()
    l = []
    with open(file,"r") as f:
        for line in f.readlines():
            line=line.strip()
            try:
                l.append(int(line))
            except:
                l.append(line)
    s.add(l[::-1],extend=True)

def grp(s):
    cur=[]
    br=s.pop()
    a=s.stack()
    s.kill()
    for i in a:
        if i == br:
            s.add(cur)
            cur=[]
            continue
        cur.append(i)
    s.add(cur)

def srt(s):
    s.add(sorted(s.pop()))

def tak(s):
    n=s.pop()
    v=s.pop()[::-1]
    s.add(v[:n])

def islst(s):
    s.add(1 if isinstance(s.pop(),list) else 0)

def count(s):
    s.add(len(s.pop()))

def rev(s):
    s.add(s.pop()[::-1])

def incdepth(s):
    s.depth(1)

def decdepth(s):
    s.depth(-1)

ops={
    ".":prh,
    ";":prs,
    "\\\\": stp,
    "+":add,
    "*":mul,
    "%":div,
    "|":grt,
    "|.":rev,
    "&":lss,
    "_":drp,
    ">":toh,
    "<":frh,
    "¬":grv,
    "'":ech,
    "/":scn,
    ".":upck,
    ",":pck,
    "!":til,
    "^":grp,
    "1:":read,
    "^.":srt,
    "#":tak,
    "#.":count,
    "?.":islst,
    "£":nop,
    ")":incdepth,
    "(":decdepth
}

