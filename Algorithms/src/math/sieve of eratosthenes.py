def criba(n):
	primes = []
	isPrime = [1 for i in range(n)]
	isPrime[0] = isPrime[1] = 0

	for i in range(n):
		if isPrime[i]:
			primes.append(i)
			h = 2
			while i*h < n:
				isPrime[i*h] = 0
				h += 1

	return primes, isPrime


from math import isqrt
def is_prime(n):
	for i in range(2,isqrt(n)+1):
		if(n%i==0):
			return False
	return True
		
for i in range(100):
	if(is_prime(i)):
		print(i)
