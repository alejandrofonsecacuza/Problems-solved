from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	n=cinint()
	a=cinline()
	l=max(a)
	r=min(a)
	return (l*(n-1))-(r*(n-1))

t=1
t=int(input())
for i in range(t):
	print(solve())
	
