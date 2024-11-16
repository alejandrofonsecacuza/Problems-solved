from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	n,b,c=cinline()
	result=c
	#if(n==1):
	if(n==1 and c!=0):
		return 1
	if(n==1 and c==0):
		return 0
	if(b==0 and c==0):
		return -1
	if(b==0):
		return n-c
	n-=c

	aux=n-(((n-1)//b)+1) 
	return c+aux
	

t=1
t=int(input())
for i in range(t):
	print(solve())
	
