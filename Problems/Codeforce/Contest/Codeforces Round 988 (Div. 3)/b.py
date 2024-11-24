from math import *
from collections import defaultdict
from collections import Counter
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def prime_factorize(n):
	"""Descompone n en factores primos.Prueba los divisores desde el número 2 hasta la raíz cuadrada del número dado.Complejidad O(√(n))"""	
	f=2
	factors=defaultdict(int)
	while(n!=1):
		if(n%f==0):
			n//=f
			factors[f]+=1
		else:
			f+=1
	return factors
# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0

	while low <= high:

		mid = (high + low) // 2

		# If x is greater, ignore left half
		if arr[mid] < x:
			low = mid + 1

		# If x is smaller, ignore right half
		elif arr[mid] > x:
			high = mid - 1

		# means x is present at mid
		else:
			return mid

	# If we reach here, then the element was not present
	return -1

# Function call
#result = binary_search(arr, x)


def solve():
	n=cinint()
	k=cinline()
	k=sorted(k)
	m=n-2
	factors=prime_factorize(m)
	factors[1]=1
	for j in factors.keys():
	#	print("bus",j)
		index=binary_search(k,j)
	#	print("find",index)
		if(index!=-1):
			k.pop(index)
	#		print("bus",m//j)
			index2=binary_search(k,m//j)
	#		print("find",index2)
			if(index2!=-1):
				return j,(m//j)
	return -1,-1
			
				
		
	
	

t=1
t=int(input())
for i in range(t):
	print(*solve())
	
