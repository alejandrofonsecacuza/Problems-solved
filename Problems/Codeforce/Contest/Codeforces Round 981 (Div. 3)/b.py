from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	n=cinint()
	N=[]
	sup=0;
	inf=0
	suma=0
	for i in range(n):
		b=cinline()
		N.append(b)
	for i in range(n):
		for j in range(abs(n-i)):
			sup=min(sup,N[j][i+j])
			inf=min(inf,N[i+j][j])
		if(i==0):
			suma+=abs(sup)
		else:
			suma+=abs(sup)+abs(inf)
		sup=0
		inf=0
	return suma
	

t=1
t=int(input())
for i in range(t):
	print(solve())
	
