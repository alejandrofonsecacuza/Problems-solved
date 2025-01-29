def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))

def find_mex(nums):
    """
    Encuentra el MEX (Minimum Excluded Value) de una lista de números enteros no negativos.

    Parámetros:
        nums (list): Lista de números enteros no negativos.

    Retorna:
        int: El MEX de la lista.
    """
    # Convertir la lista a un set para búsquedas eficientes (O(1))
    num_set = set(nums)
    
    # Iterar desde 0 hasta len(nums) + 1 para encontrar el MEX
    for i in range(len(nums) + 1):
        if i not in num_set:
            return i
    
def solve():
    n,m,k=cinline()
    lm=cinline()
    lk=cinline()
    ###
    if(k==n):
        return "1"*m
    if(n-k!=1):
        return "0"*m
    response=["0"]*m
    mex=find_mex([0]+lk)
    try:
        index=lm.index(mex)

        response[index]="1"
    except:
        pass
    return "".join(response)
t=1
t=cinint()
for _ in range(t):
    print(solve())