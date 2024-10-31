from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	n,m,r,c=cinline()
	size=n*m
	num=(r-1)*m+c
	resto=(size-num)
	salto=resto//m
	res=salto*m+(resto-salto)
	return res
	

t=1
t=int(input())
for i in range(t):
	print(solve())
		
