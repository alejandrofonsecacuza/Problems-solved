from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def is_prime(n):
	for i in range(2,isqrt(n)+1):
		if(n%i==0):
			return False
	return True

def solve():
	n=cinint()
	i=2
	response=[]
	#imprimiendo pares
	for i in range(2,n+1,2):
		response.append(i)
	
	#buscando un impar que sumado con el ultimo par sea compuesto
	j=1
	band=False
	for j in range(1,n+1,2):
		if(not is_prime(i+j)):
			band=True
			break
	if(not band):
		return [-1]
	
	response.append(j)
	for k in range(1,n+1,2):
		if(k==j):continue
		response.append(k)
		
	return response
		

t=1
t=int(input())
for i in range(t):
	print(*solve())
	
