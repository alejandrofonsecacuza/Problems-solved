from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	n=cinint()
	l=[]
	a_max,b_max=0,0
	for i in range(n):
		a,b=cinline()
		a_max=max(a,a_max)
		
		b_max=max(b,b_max)
	return (a_max+b_max)*2	
	
	

t=1
t=int(input())
for i in range(t):
	print(solve())
	
