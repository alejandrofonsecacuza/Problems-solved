#xcvojnzdfpiwqnjxtvwgklbveobrhbijjtyjthdzsgtnycvpdiaozmxdhgohpqtpymvwktrzrznybtqfabasdqxfppjndbctedqx

from collections import Counter
def fact(n,MOD=(10**9)+7):
	"""O(n)"""
	response=[1]*(n+1)
	response[0]=1
	for i in range(1,n+1):
		response[i]=((response[i-1]%MOD) *(i % MOD))%MOD
	return response

factorial=fact(1000000)



def count_rep(s):
    counter=Counter(list(s))
    d=1
    for _,val in counter.items():
        d*=factorial[val]
    return d


s=input()
n=len(s)

aux=count_rep(s)

print(factorial[n]//aux)
