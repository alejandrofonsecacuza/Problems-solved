from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	n=cinint()
	if(n%2!=0):
		if(n==1):
			print(1)
			print(1)
			return
		if(n==3):
			print(2)
			print(1,2,3)
			return
		print(n)
		for i in range(1,n):
			if(i==1 or i==3 or i==(n-1) or i==n):
				continue
			else:
				print(i,end=" ")
		print(1,3,n-1,n)
		return
	else:
		s=[]
		l=int(log(n,2))
		vis=0
		if(n&(n-1)):
			vis=(1<<l)-1
			for i in range(1,n-1):
				if(i!=vis):
					s.append(i)
			s.append(n)
			s.append(n-1)
			s.append(vis)
			print((1<<(l+1))-1)
		else:
			if(n>=8):
				for i in range(2,n-2):
					if(i!=3):
						s.append(i)
				s.append(1)
				s.append(3)
				s.append(n-2)
				s.append(n-1)
				s.append(n)
				print((1<<(l+1))-1)
			if(n==4):
				for i in range(1,n):
					s.append(i)
				print(6)
			if(n==2):
				for i in range(1,n):
					s.append(i)
				print(2)
		print(*s)
		

t=1
t=int(input())
for i in range(t):
	solve()
	
