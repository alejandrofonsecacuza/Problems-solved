from itertools import permutations,combinations
def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))

from itertools import permutations

def maximize_S_and_get_kth():
    n,k=cinline()
    # Generar la permutación que maximiza S(p)
    nums = list(range(1, n + 1))
    #print(f"{nums=}")
    nums.sort(reverse=True)
    #print(f"{nums=}")

    optimal_perm = []
    while nums:
        if len(optimal_perm) % 2 == 0:
            optimal_perm.append(nums.pop(0))
        else:
            optimal_perm.append(nums.pop())
    #print(f"{optimal_perm=}")
    
    
    # Generar todas las permutaciones con el mismo S(p) máximo
    perms = sorted(permutations(optimal_perm))
    #print(f"{perms=}")

    # Si k es mayor que el número total de permutaciones
    if k > len(perms):
        return "No existe tal permutación"
    #print(k-1)
    # Devolver la k-ésima permutación (1-indexada)
    return perms[k - 1]

t=1
t=cinint()
for _ in range(t):
    print(*maximize_S_and_get_kth())