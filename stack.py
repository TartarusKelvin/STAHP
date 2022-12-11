class stack():
    def __init__(self) -> None:
        self.items=[]

    def pop(self):
        return self.items.pop()
    
    def add(self,x,extend=False):
        if extend:
            self.items.extend(x)
            return
        if isinstance(x,op):
            # We have an operator
            if x.df == 0:
                x.func(self)
                return 
        self.items.append(x)

    def kill(self):
        self.items=[]
    
    def stack(self):
        return self.items

    def count(self):
        return len(self.items)

    def peak(self):
        if self.count() == 0:
            return None
        return self.items[-1]
    
class op():
    def __init__(self,func,token,df=0) -> None:
        self.func = func
        self.df=df
        self.token=token

    def __repr__(self):
        d="".join(["`" for x in range(self.df)])
        return d+self.token
