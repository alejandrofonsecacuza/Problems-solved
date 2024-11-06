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
def Sieve_of_Eratosthenes(n):
    sieve=[True]*n
    sieve[0]=False
    sieve[1]=False
    for i in range(2,isqrt(n)):
    	if(sieve[i]):
    		for j in range(i+i,n,i):
    			sieve[j]=False
    return	sieve


from math import isqrt
def is_prime(n):
	for i in range(2,isqrt(n)+1):
		if(n%i==0):
			return False
	return True
