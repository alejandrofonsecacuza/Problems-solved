
import bisect

def lower_bound(arr, x):
	"""devuelve el índice de la primera posición donde el valor dado puede ser insertado sin romper el orden. En otras palabras, busca el primer índice donde el valor es mayor o igual al elemento dado."""
	return bisect.bisect_left(arr, x)

def upper_bound(arr, x):
	"""devuelve el índice de la posición justo después del último valor igual al valor dado. """
	return bisect.bisect_right(arr, x)
			
l=[1,2,33,43,53,62,71]

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
if __name__=="__main__":
    print(find_max_le_index(l,42))