from math import *
from functools import reduce
mul=lambda x,y:x*y
def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
total=0

def generate_subsets(arr,num):
    global total
    n = len(arr)
    for i in range(1 << n):
        subset = [arr[j] for j in range(n) if (i & (1 << j)) != 0]
        if(not subset):continue
        aux=reduce(mul,subset)
        total+=(num//aux)*(-1 if (len(subset)%2==0) else 1)
    return total
def solve():
    global total
    n,k=cinline()
    a=cinline()
    generate_subsets(a,n)
    return total
t=1
#t=int(input())
for i in range(t):
    print(solve())
    
