from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	a=cinline()
	return max(a)
	

t=1
t=int(input())
for i in range(t):
	print(f"Case {i+1}:",solve())
	
