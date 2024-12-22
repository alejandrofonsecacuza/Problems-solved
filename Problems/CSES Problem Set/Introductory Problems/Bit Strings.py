
from math import *

MOD=(10**9)+7
def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def fast_pow(a,b):
    """ return a^b"""
    if(b==0):return 1
    if(b==1):return a
    
    if(b%2==0):
        result=fast_pow(a,b//2)
        return (result*result)%MOD
    else:
        result=fast_pow(a,b//a)
        return (result*result*a)%MOD
def solve():
    n=cinint()
    return fast_pow(2,n)


t=1
#t=int(input())
for i in range(t):
    print(solve())