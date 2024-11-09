def g(F,C):
    n=max([F,C])
    return (n*(n-1))+1
    
def solve():
    F,C=map(int,input().split())
    D=g(F,C)
    if(C==F):
        return D
    if(C>F):
        if(C%2==0):
            return D-(C-F)
        else:
            return D+(C-F)
    if(C<F):
        if(F%2==0):
            return D+(F-C)
        else:
            return D-(F-C)
 
        
t=int(input())
for i in range(t):
    print(solve())
