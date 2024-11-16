#from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))
from collections import defaultdict
def solve():
    a=cinline()

    for i in range(5):
        a=sorted(a)
        a[0]+=1
    return a[0]*a[1]*a[2]
		
	

t=1
t=int(input())
for i in range(t):
    print(solve())