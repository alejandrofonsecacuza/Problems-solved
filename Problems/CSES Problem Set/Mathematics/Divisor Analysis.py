from functools import reduce
def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
MOD=(10**9)+7
def fast_pow(a, b):
	if b == 0: return 1
	s = fast_pow(a, b//2)
	if b%2 == 0: return (s*s)%MOD
	else: return (s*s*a)%MOD
def fast_pow2(a, b):
	if b == 0: return 1
	s = fast_pow(a, b//2)
	if b%2 == 0: return (s*s)
	else: return (s*s*a)
"""
5
2 790809628
3 626807588
5 488751710
7 965067804
11 26375222
"""
def sum_divisors(factors):
    response=1
    for key,value in factors.items():
        response*=(((fast_pow(key,value+1)-1)%MOD)*(fast_pow((key-1),(MOD-2))%MOD)) 
    return response%MOD

def mul_divisors(factors,sum):
    response=1
    for factor,power in factors.items():
        response*=fast_pow(factor,(euler_sum(power)*(sum/(power+1))))
    return response%MOD
    pass
def euler_sum(n):
    return (n*(n+1))/2

def solve():
    n=cinint()
    factors={}
    response_count_factors=1
    for _ in range(n):
        x,k=cinline()
        response_count_factors*=(k+1)
        factors[x]=k
    #print("debug1")
        
    response_sum=sum_divisors(factors=factors)
    #print("debug2")

    response_mul=mul_divisors(factors=factors,sum=response_count_factors)
    #print("debug3")
    
    return response_count_factors%MOD,int(response_sum%MOD),response_mul%MOD


    pass
t=1
for _ in range(t):
    print(*solve())