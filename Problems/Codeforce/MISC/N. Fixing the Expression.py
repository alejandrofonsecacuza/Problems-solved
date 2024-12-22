from math import *
def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))

def solve():
    exp=input()
    a,b=exp[0],exp[2]
    if(a==b):
        return f"{a}={b}"
    elif(a<b):
        return f"{a}<{b}"
    else:
        return f"{a}>{b}"

t=1
t=int(input())
for i in range(t):
    print(solve())
    
