from collections import defaultdict
def prime_factorize(n):
	f=2
	factors=defaultdict(int)
	while(n!=1):
		if(n%f==0):
			n//=f
			factors[f]+=1
		else:
			f+=1
	return factors


def count_factors(n):
	factors=prime_factorize(n)
	response=1
	for f in factors.values():
		response*=(f+1)
	return response

print(prime_factorize(33))

print(prime_factorize(66))
