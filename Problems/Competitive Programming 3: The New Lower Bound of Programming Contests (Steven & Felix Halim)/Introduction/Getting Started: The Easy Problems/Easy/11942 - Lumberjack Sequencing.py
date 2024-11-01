from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
	a=cinline()
	if a[0]>a[1]:
		for i in range(9):
			if(a[i]<a[i+1]):
				return "Unordered"
		return "Ordered"
	else:
		for i in range(9):
			if(a[i]>a[i+1]):
				return "Unordered"
		return "Ordered"
	
		

t=1
t=int(input())
print("Lumberjacks:")

for i in range(t):
	print(solve())
	
