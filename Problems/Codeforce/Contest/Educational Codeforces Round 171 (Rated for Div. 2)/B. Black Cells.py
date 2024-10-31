from math import *
from collections import defaultdict
from itertools import *

def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	n=cinint()
	a=cinline()
	if(n==1):
		return 1
	if(n%2==0):
		s=set()
		for i in range(2,n+1,2):
			sub=a[i-2:i]
			dis=abs(sub[0]-sub[1])
			s.add(dis)
		s=sorted(s,reverse=True)	
		
		return s[0]
			
	else:

		response=[]
		
		for j in combinations(a,n-1):
			#print(j)
			s=set()
			for i in range(2,n+1,2):
				sub=j[i-2:i]
				#print(a[i-2:i])
				dis=abs(sub[0]-sub[1])
				s.add(dis)
			s=sorted(s,reverse=True)
			#print(s)
			response.append(s[0])
		return min(response)
			
			
	
t=1
t=int(input())
for i in range(t):
	print(solve())
	
