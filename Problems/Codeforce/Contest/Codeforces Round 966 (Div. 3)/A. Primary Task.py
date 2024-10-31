from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	n=input()
	if(len(n)<=2):
		return "NO"

	if(n[:2]!="10"):
		return "NO"
	m=n[2:]
	if(m[0]=="0"):
		return "NO"
	if(int(m)>=2):
		return "YES"
	else:
		return "NO"
	pass
	

t=1
t=int(input())
for i in range(t):
	print(solve())
	
