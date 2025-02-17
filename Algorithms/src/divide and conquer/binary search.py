l=[1,2,33,43,53,62,71]

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
	# If we reach here, then the element was not present

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

			
