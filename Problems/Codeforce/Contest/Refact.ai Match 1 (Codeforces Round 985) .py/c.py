from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

#Maximum sum subarray
def Maximum_sum_subarray(arr):
	contador=0
	l=-1
	r=-1
	mayor=-1*float("inf")
	m_l,m_r=-1,-1
	for ind,i in enumerate(arr):
		contador+=i
		if(l==-1):
			l=ind
		r=ind
		if contador<0:
			l,r=-1,-1
			contador=0
		elif contador>=mayor:
			if(l==-1):
				l=ind
			m_l,m_r=l,r
			mayor=contador
	return mayor,(m_l,m_r)
	
def solve():
	n=cinint()
	a=cinline()
	#a=[1, 2, 3, 4, 5, 4, 3, 2, 1,0, 4,5,6,7,8,9,10,1,2,3,4,4,4,5,6,5]
	#n=len(a)
	x=0
	
	arr=[]
	for i in a:
	#	print(x)
		if i>x:
			arr.append(-1)
			x+=1
		elif i<x:
			arr.append(1)
			x-=1
		else:
			arr.append(1)
	#print(arr)
	_,r=Maximum_sum_subarray(arr)
	#print(_)
	#print(r)

	if(r==(-1,-1)):
		return x-1
	x=0
	for index,i in enumerate(a):
		if(index<r[0] or index>r[1]):
			if i>x:
				x+=1
			elif i<x:
				x-=1
	return x

t=1
t=int(input())
for i in range(t):
	print(solve())
	
