from math import *
from collections import Counter
def cinint():
	return int(input())
def cinline():
	return list(map(int,list(input())))

def solve():
	n=cinint()
	s=cinline()
	r=cinline()
	m=Counter(s)
	
	
	cant_0=m[0]
	cant_1=m[1]
	#print(cant_0)
	#print(cant_1)
	if(cant_0<=0 or cant_1<=0):	
		return "NO"
	for i in r[:-1]:
		if(i):
			cant_0-=1
		else:
			cant_1-=1
		if(cant_0<=0 or cant_1<=0):	
			return "NO"
	return "YES"
			
			
	
t=1
t=int(input())
for i in range(t):
	print(solve())
	
