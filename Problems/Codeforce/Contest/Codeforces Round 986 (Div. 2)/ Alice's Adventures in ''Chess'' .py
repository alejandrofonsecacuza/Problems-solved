from itertools import cycle
from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

"""
go north (represented by N), moving to (x,y+1)
;
go east (represented by E), moving to (x+1,y)
;
go south (represented by S), moving to (x,y−1)
; or
go west (represented by W), moving to (x−1,y)
.
"""
def solve():
	n,a,b=cinline()
	s=list(input())
	p=[0,0]
	count=0
	for i in range(1000):
		j=s[count%len(s)]
		if(j=="N"):
			p[1]+=1
		elif(j=="E"):
			p[0]+=1
		elif(j=="S"):
			p[1]-=1
		elif(j=="W"):
			p[0]-=1
		count+=1
		if(p[0]==a and p[1]==b):	
			return "YES"
	return "NO"
				

t=1
t=int(input())
for i in range(t):
	print(solve())
	
