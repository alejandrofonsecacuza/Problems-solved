from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	n=cinint()
	calls=cinline()
	mile=0
	juice=0
	for c in calls:
		mile+= c//30 + 1
		juice+= c//60 +1
	
	
	if (mile*10 < juice*15):
		return f"Mile {mile*10}" 
	elif (mile*10 > juice*15):
		return f"Juice {juice*15}"
	elif (mile*10 == juice*15):
		return f"Mile Juice {juice*15}"
	

t=1
t=int(input())
for i in range(t):
	print(f"Case {i+1}: {solve()}")
	




