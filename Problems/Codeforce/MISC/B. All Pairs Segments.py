from math import *
from collections import defaultdict
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def calc(p,n):
	return (p*(n-p+1))-1
def solve():
	n,q=cinline()
	x=cinline()
	k=cinline()
	count_p=defaultdict(int)

	for i in range(1,n+1):
		count_p[calc(i,n)]+=1
	count=0
	aux=None		
	for i in x:
		if(aux):
			count_p[count*(n-count)]+=abs(i-aux)-1
		count+=1
		aux=i
	#print(count_p)
	response=[]
	for q in k:
		r=count_p.get(q,False)
		if(r):
			response.append(r)
		else:
			response.append(0)
	return response

t=1
t=int(input())
for i in range(t):
	print(*solve())
	

