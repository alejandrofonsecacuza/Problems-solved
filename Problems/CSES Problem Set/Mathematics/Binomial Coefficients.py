def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))
def fast_pow_with_module(a, b,MOD=(10**9)+7):
	if b == 0: return 1
	s = fast_pow_with_module(a, b//2)
	if b%2 == 0: return (s*s)%MOD
	else: return (s*s*a)%MOD

def fact(n,MOD=(10**9)+7):
	"""O(n)"""
	response=[1]*(n+1)
	for i in range(1,n+1):
		response[i]=((response[i-1]%MOD) *(i % MOD))%MOD
	return response

factorial=fact(1000000)

def binomial_coefficients(n,k,MOD=(10**9)+7):
	global factorial
	return factorial[n]*fast_pow_with_module((factorial[n-k]*factorial[k]),(MOD-2))%MOD
	

	
def solve():
	MOD=(10**9)+7
	a,b=cinline()
	return binomial_coefficients(a,b)%MOD

#t=1
t=int(input())
for i in range(t):
	print(solve())
	
