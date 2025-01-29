
def binary_search(arr, x, k,visited):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:

        mid = (high + low) // 2

		# If x is greater, ignore left half
        if arr[mid] < (x-k):
            low = mid + 1

		# If x is smaller, ignore right half
        elif arr[mid] > (x+k):
            high = mid - 1

		# means x is present at mid
        else:
            if visited[mid]:
                 high = mid - 1
            else:
                return mid
    return -1

def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
from collections import Counter
def solve():
    n,m,k=cinline()
    la=cinline()
    lb=cinline()
    lb=sorted(lb)
    la=sorted(la)
    response=0
    index_a=0
    index_b=0
    while index_a < n and index_b < m:
        if (la[index_a]+k) >= lb[index_b] and lb[index_b] >= (la[index_a]-k):
            response+=1
            index_b+=1
            index_a+=1
        elif lb[index_b] > (la[index_a]+k):
            index_a+=1
        elif lb[index_b] < (la[index_a]-k):
            index_b+=1
    return response
            
            
    

            
        


t=1 
#t=cinint()
for _ in range(t):
    print(solve())