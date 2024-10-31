from math import *

def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	n=cinint()
	s=""
	
	s+="0"*(n-1)
	s+="1"
	return s
	return 
t=1
t=int(input())
for i in range(t):
	print(solve())
	
