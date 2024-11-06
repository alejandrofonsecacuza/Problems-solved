from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	n=cinint()
	memo=["$"]
	pos=0
	for i in range(n):
		a=input()
		#print(memo)
		if(a=="LEFT"):
			pos-=1
			memo.append(-1)	
		elif(a=="RIGHT"):
			pos+=1
			memo.append(1)
		else:
			num=int(a.split()[-1])
			#print("num",num)
			pos+=memo[num]
			memo.append(memo[num])
	return pos
	

t=1
t=int(input())
for i in range(t):
	print(solve())
	
