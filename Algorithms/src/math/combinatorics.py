from itertools import *
#from math import factorial

def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def count_permutation(n, k):
    return factorial(n) // factorial(n - k)
   	
def count_combinations(n,k):
	return factorial(n) // (factorial(k)*factorial(n - k))

def generate_subsets(arr):
    n = len(arr)
    subsets = []
    for i in range(1 << n):
        subset = [arr[j] for j in range(n) if (i & (1 << j)) != 0]
        subsets.append(subset)
    return subsets
k=1
l=[1,2,3,4,5]
#Permutaciones P(l):Genera todas las permutaciones de l
permutations(l,len(l))
#Variacion V(l,k) :Genera todas las permutaciones de tamannio k en la lista l
permutations(l,k)
#Combinaciones C(l,k) :Genera todas las formas de escoger k elementos en la lista l
combinations(l,k) 

"""
A sequence a is a subsequence of a sequence b if a can be obtained from b by the deletion of several (possibly, zero or all) elements.
"""
l=[]
def subsequence(l):
	response=[]
	for i in range(1,len(l)+1):
		response+=list(combinations(l,i))
	return response
for i in subsequence(l):
	print(i)
		
