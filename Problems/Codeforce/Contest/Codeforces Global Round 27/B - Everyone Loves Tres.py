from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	n=cinint()
	if(n==2):
		return 66
	if(n<4):
		return -1
	s=""
	for i in range(n-4):
		if(i%2==0):
			s+="5"
		else:
			s+="0"
	s+="51"
	return int(s)*66

	

t=1
t=int(input())
for i in range(t):
	print(solve())
	
