from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	l,r,k=cinline()
	aux=(r//k)-l+1
	return aux if aux>=0 else 0
			
	

t=1
t=int(input())
for i in range(t):
	print(solve())
	
