def find_max_le_index(sorted_arr, a):
    # Búsqueda binaria para encontrar el mayor elemento <= a
    left, right = 0, len(sorted_arr) - 1
    best_index = -1

    while left <= right:
        mid = (left + right) // 2
        if sorted_arr[mid] <= a:
            best_index = mid  # Actualizamos el mejor índice
            left = mid + 1  # Buscamos hacia la derecha
        else:
            right = mid - 1  # Buscamos hacia la izquierda

    # Retornamos el índice del mayor elemento <= a, o -1 si no existe
    return best_index
	# If we reach here, then the element was not present

def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
from collections import Counter
def solve():
    n,m_ = cinline()#0(1)
    a   = cinline()#0(n)
    b   = cinline()#0(m)
    a   = sorted(a)#O(nlog(n))
    cnt=Counter(a)#O(n)
    keys=list(cnt.keys())#O(n)
    for i in b:#O(m)
        index=find_max_le_index(keys,i)#O(log(n))
        if index!=-1:
            print(keys[index])#0(1)
            cnt[keys[index]]-=1#0(1)
            if not cnt[keys[index]]:#0(1)
                del cnt[keys[index]]#O(1)
                keys.pop(index)
        else:
            print(-1)#0(1)
        
t=1
for _ in range(t):#0(1)
    (solve())