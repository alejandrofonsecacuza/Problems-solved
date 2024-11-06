from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	n=cinint()
	a=cinline()
	for i in range(n-1):
		aux=abs(a[i]-a[i+1])
		#print(aux)
		if(aux==5 or aux==7):
			continue
		else:
			return "NO"
	return "YES"
			
	

t=1
t=int(input())
for i in range(t):
	print(solve())
	
