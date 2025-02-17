#C(n,k)= n!/(k!(n-k)!)
#from combinatorics import count_combinations
from math import factorial
def fact(n,MOD=(10**9)+7):
	"""O(n)"""
	response=[1]*(n+1)
	response[0]=1
	for i in range(1,n+1):
		response[i]=((response[i-1]%MOD) *(i % MOD))%MOD
	return response

	
import time
start=time.time()
factorial=factorial(99)
print(f'{str(factorial)[-23:]=}')



end=time.time()
print((end-start))



