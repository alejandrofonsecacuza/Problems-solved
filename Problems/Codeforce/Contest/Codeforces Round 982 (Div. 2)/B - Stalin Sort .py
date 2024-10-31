from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	n=cinint()
	l=cinline()
	l_order=sorted(l,reverse=True)
	
	response=float("inf")
	for index,value in enumerate(l_order):
		response=min(l.index(value)+index,response)
	return response
		
	pass
	

t=1
t=int(input())
for i in range(t):
	print(solve())
	
