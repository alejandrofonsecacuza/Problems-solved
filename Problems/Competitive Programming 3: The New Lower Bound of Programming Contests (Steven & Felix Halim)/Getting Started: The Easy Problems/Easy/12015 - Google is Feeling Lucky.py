from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	urls=[]
	rel=[]
	for i in range(10):
		s,r=input().split()
		urls.append(s)
		rel.append(int(r))
	maximo=max(rel)
	response=[]
	for ind,value in enumerate(rel):
		if(value==maximo):
			print(urls[ind])
	
		
	
t=1
t=int(input())
for i in range(t):
	print(f"Case #{i+1}:")
	solve()
	
	
