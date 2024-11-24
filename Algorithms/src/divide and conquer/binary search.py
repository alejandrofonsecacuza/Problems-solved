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

	# If we reach here, then the element was not present

import bisect

def lower_bound(arr, x):
	"""devuelve el índice de la primera posición donde el valor dado puede ser insertado sin romper el orden. En otras palabras, busca el primer índice donde el valor es mayor o igual al elemento dado."""
	return bisect.bisect_left(arr, x)

def upper_bound(arr, x):
	"""devuelve el índice de la posición justo después del último valor igual al valor dado. """
	return bisect.bisect_right(arr, x)
#lista = [1, 3, 4, 4, 7, 8, 10]
#x = 7
#print(lower_bound(lista,x))
#print(upper_bound(lista,x))



			
