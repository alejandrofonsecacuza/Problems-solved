from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	n=cinint()
	a=cinline()
	l=0
	c=0
	for index in range(n-1):
		if(a[index]<a[index+1]):
			l+=1
		elif(a[index]>a[index+1]):
			c+=1
	return l,c	
t=1
t=int(input())
for i in range(t):
	print(f"Case {i+1}:",*solve())
	
