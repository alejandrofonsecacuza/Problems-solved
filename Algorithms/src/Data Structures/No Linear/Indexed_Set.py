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
    n=cinint()
    a=cinline()
    b=cinline()
    a=sorted(a)
    cnt=Counter(a)
    print(cnt.keys())
    for i in b:
        #print(f'{i=}')
        index=find_max_le_index(list(cnt.keys()),i)
        #print(f'{index=}')
        print(index)
        if index!=-1:
            cnt[index]-=1
            if not cnt[index]:
                del cnt[index]
        

    
        
    pass
t=1
#t=cinint()
for _ in range(t):
    print(solve())