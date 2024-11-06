#from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))
from collections import defaultdict
def solve():
	n,k=cinline()
	a=defaultdict(int)	
	
	result1=0
	
	for i in range(k):
		bi,ci=cinline()
		a[bi]+=ci
		result1+=ci
		
	if(n>=len(a)):
		return result1
	else:
		return sum(sorted(a.values(),reverse=True)[:n])
		
	

t=1
t=int(input())
for i in range(t):
	print(solve())
	
