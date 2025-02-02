def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))

import bisect

def find_max_not_greater(arr, x):
    """
    Retorna el índice del elemento máximo no mayor que x.
    Si todos los elementos son mayores que x, retorna -1.
    Si la lista está vacía, retorna -1.
    """
    if not arr:
        return -1  # Lista vacía
    index = bisect.bisect_right(arr, x) - 1
    return index if index >= 0 else -1

def find_min_not_less(arr, x):
    """
    Retorna el índice del elemento mínimo no menor que x.
    Si todos los elementos son menores que x, retorna len(arr).
    Si la lista está vacía, retorna 0.
    """
    if not arr:
        return 0  # Lista vacía
    index = bisect.bisect_left(arr, x)
    return index if index < len(arr) else len(arr)

			

def solve():
    n=cinint()
    a=cinline()
    q=cinint()
    a.sort()
    result=[]
    for _ in range(q):
        l,r = cinline()
        ind1=find_min_not_less(a,l)
        ind2=find_max_not_greater(a,r)
        result.append(ind2-ind1+1)
    return result
t=1
#t=cinint()
for _ in range(t):
    print(*solve())