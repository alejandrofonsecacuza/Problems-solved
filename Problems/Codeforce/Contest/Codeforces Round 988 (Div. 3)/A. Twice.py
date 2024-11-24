from math import *
from collections import Counter
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	n=cinint()
	a=cinline()
	response=0
	for i in  Counter(a).values():
		response+=i//2
	return response
	
	

t=1
t=int(input())
for i in range(t):
	print(solve())
	
