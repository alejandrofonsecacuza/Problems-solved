from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))
def E(n):
	a=(n*(n-1))/2
	return a if (a) else 1 
	
def solve():
	n=cinint()
	response=0
	index=-1
	for i in range(2,n+1):
		aux=i*E(floor(n/i)+1)
		if(aux>response):
			index=i
			response=aux		
	return index
	

t=1
t=int(input())
for i in range(t):
	print(solve())
	
