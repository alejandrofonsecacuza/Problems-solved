from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

from collections import Counter
def solve():
	n=cinint()
	a=cinline()
	m=cinint()
	
	list_par={j:[] for j in a}
	for ind,elem in enumerate(a):
		list_par[elem].append(ind)
	#print(list_par)
	
	
	for i in range(m):
		s=input()
		#print(len(s))
		dp={}
		if(len(s)>n or len(s)<n):
			print("NO")
			continue
		band2=False
		for value,pos in list_par.items():
			#print(dp)
			if(band2):
				break
			
			aux=s[pos[0]]
			band2=False
			band=False
			if(dp.get(aux,False)):
				band=True
				print("NO")
				break
			dp[aux]=value
			for p in pos[1:]:
				if(s[p]!=aux):
					band=True
					band2=True
					print("NO")
					break
		if(band==False):
			print("YES")
t=1
t=int(input())
for i in range(t):
	solve()
	
