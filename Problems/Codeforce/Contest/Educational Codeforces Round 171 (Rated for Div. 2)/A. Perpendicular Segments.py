from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))
def find_segments(X, Y, K):
	if(K<=X and K<=Y):
		AB=(0,0,0,K)
		CD=(0,0,K,0)
	else:
		Z=min(X,Y)
		AB=(0,0,Z,Z)
		CD=(0,Z,Z,0)
	# Retornamos los segmentos
	return AB,CD

def solve():
	X,Y,K=cinline()
	AB,CD= find_segments(X,Y,K)	
	print(*AB)
	print(*CD)



t=1
t=int(input())
for i in range(t):
	solve()
	
