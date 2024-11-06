from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	s=list(input())
	#print(s)
	n=len(s)
	results=[]
	q=cinint()
	
	count_1100 = 0
	for i in range(n - 3):
		if s[i:i+4] == ["1","1","0","0"]:
			count_1100 += 1
	        
	queries = []
	for __ in range(q):
		i, v = cinline()

		i-=1
		affected_indices = range(max(0, i - 3), min(n - 3, i) + 1)
		for j in affected_indices:
			if s[j:j+4] == ["1","1","0","0"]:
				count_1100 -= 1
		s[i]=str(v)
		
		for j in affected_indices:
			if s[j:j+4] == ["1","1","0","0"]:
				count_1100 += 1
		if count_1100 > 0:
			print("YES")
			
		else:
			print("NO")

t=1
t=int(input())
for i in range(t):
	solve()
	
