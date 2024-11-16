from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	n=cinint()
	response=0
	for i in range(n):
		a,b,c=cinline()
		response+=((a/b)*c)*b
	return int(response)
	

t=1
t=int(input())
for i in range(t):
	print(solve())
	
