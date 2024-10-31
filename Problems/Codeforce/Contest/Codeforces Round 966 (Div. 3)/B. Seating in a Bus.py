from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	n=cinint()
	a=cinline()
	o=[0]*(2*n)
	o[a[0]]=1
	for i in a[1:]:
		if(o[i+1] or o[i-1]):
			o[i]=1
		else:
			return "NO"
	return "YES"


t=1
t=int(input())
for i in range(t):
	print(solve())
	
