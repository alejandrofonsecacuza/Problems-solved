from math import *
from itertools import cycle
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	n=cinint()
	names=[]
	for i in range(n):
		names.append(input())
	song=["Happy", "birthday", "to" ,"you" ,"Happy", "birthday" ,"to", "you", "Happy", "birthday", "to", "Rujia", "Happy", "birthday", "to", "you"]
	index=0
	index2=0
	
	for name in cycle(names):
		print(f"{name}: {song[index]}")
		index+=1
		index2+=1
		if(index==16 and index2>=n):
			break
		elif(index==16 and index2<n):
			index=0	

t=1
#t=int(input())
for i in range(t):
	solve()
	
