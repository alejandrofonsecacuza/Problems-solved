from math import *
from collections import defaultdict
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

MOD=(10**9)+7
def criba(n):
	"""Retorna una lista con los numeros primos hasta n y otra con que numero hasta n es primo o no. O(nloglogn)"""
	primes = []
	isPrime = [1 for i in range(n+1)]
	isPrime[0] = isPrime[1] = 0

	for i in range(n+1):
		if isPrime[i]:
			primes.append(i)
			h = 2
			while i*h < (n+1):
				isPrime[i*h] = 0
				h += 1

	return primes, isPrime

def prime_factorize_with_sieve(primes,n):
	factors=defaultdict(int)
	i=0
	while(n!=1):
		while(n%primes[i]==0):
			n/=primes[i]
			factors[primes[i]]+=1
		i+=1
	return factors

def sum_divisors(factors):
	response=1
	
	for key,value in factors.items():
		sum_aux=0
		for exp in range(value+1):
			sum_aux+=(key**exp)
		response*=sum_aux
	return response
def fast_pow(a, b):
	if b == 0: return 1
	s = fast_pow(a, b//2)
	if b%2 == 0: return s*s
	else: return s*s*a

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


def solve():
	global MOD
	#n=cinint()
	#PRIMES,_=criba(n)#O(√(n)LogLog(n))
	#print(PRIMES)
	response=0

	a=[3,6,12,24]
	for i  in a:
		print(sum_divisors(prime_factorize(i)))

t=1
#t=int(input())
for i in range(t):
	print(solve())
	
