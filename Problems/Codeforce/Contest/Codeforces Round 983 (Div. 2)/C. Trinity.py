from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	n=cinint()
	a=cinline()
	a=sorted(a)
	m=a[-1]
	response=0
	
	for i in range(len(a)):
		if a[i]+a[i+1] >m:
			p=i
			break
	return p
	
t=1
t=int(input())
for i in range(t):
	print(solve())
	
