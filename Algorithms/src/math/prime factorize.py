from collections import defaultdict

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


#Una mejora utilizando la Criba de Eratóstenes

#1. Generar todos los números primos hasta  n  utilizando la Criba de Eratóstenes.

#2. Utilizar esos números primos para descomponer  n  en sus factores primos.

from sieve_of_eratosthenes import criba

def prime_factorize_with_sieve(primes,n):
	factors=defaultdict(int)
	i=0
	while(n!=1):
		while(n%primes[i]==0):
			n/=primes[i]
			factors[primes[i]]+=1
		i+=1
	return factors

n=30
primes,_=criba(n)
print(primes)

print(prime_factorize_with_sieve(primes,n))
		
			


def count_factors(n):
	factors=prime_factorize(n)
	response=1
	for f in factors.values():
		response*=(f+1)
	return response

