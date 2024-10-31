from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	n=cinint()
	if(n%2==0):
		return "Sakurako"
	else:
		return "Kosuke"
	pass
	

t=1
t=int(input())
for i in range(t):
	print(solve())
	
