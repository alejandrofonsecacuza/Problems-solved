from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

MOD=(10**9)+7
def f(i,m):
	n=m-1
	return ((n-i+1)*(n+i))//2

def sum_of_divisors(n): 
	global MOD
	count=0
	i=1
	liminf=n
	limsup=n
	while(i*i<=n):
		aux=n//i
		count+=((i*aux)%MOD)
		limsup=liminf
		liminf=aux+1
		count+=((f(liminf,limsup)*(i-1))%MOD)
		i+=1
		#print(liminf,limsup,aux,count)
	if((i-1)!=aux):
		count+=(i*(n//i))%MOD
	return int(count)

def solve():
	global MOD
	n=cinint()
	return sum_of_divisors(n)%MOD
print(solve())
