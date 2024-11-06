from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	n=cinint()
	a=cinline()
	ones=sum(a)
	mini=0
	
	if(ones%2==0):
		mini=0
	else:
		mini=1
	maxi=min(ones,len(a)-ones)
	
	return mini,maxi
	

t=1
t=int(input())
for i in range(t):
	print(*solve())
	
