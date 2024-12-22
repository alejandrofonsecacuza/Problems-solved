#E. Beautiful Array
from math import *
def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))

def solve():
    a,b=cinline()
    response=[0]*3
    response[1]=b
    aux=a*3
    response[2]=b
    response[0]=aux-(2*b)
    return response
        
        

#t=1
t=int(input())
for i in range(t):
    print(*solve())
    
    
