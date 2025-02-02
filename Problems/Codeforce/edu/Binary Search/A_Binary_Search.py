def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))

def binary_search(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0

	while low <= high:

		mid = (high + low) // 2

		# If x is greater, ignore left half
		if arr[mid] < x:
			low = mid + 1

		# If x is smaller, ignore right half
		elif arr[mid] > x:
			high = mid - 1

		# means x is present at mid
		else:
			return mid
	return -1
	# If we reach here, then the element was not presenta

def solve():
    n,q=cinline()
    a=cinline()
    
    query=cinline()
    for i in query:
        if(binary_search(a,i)!=-1):
            print("YES")
        else:
            print("NO")
t=1
#t=cinint()
for _ in range(t):
    (solve())