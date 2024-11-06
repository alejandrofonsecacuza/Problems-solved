l=[1,2,33,43,53,62,71]


def binary_search(arr,elem):
	"""O(log<2><len(arr)>)"""
	r=0
	l=len(arr)-1
	while(r<l and abs(r-l)!=1):
		m=(l+r)//2
		if(arr[m]<elem):
			r=m
		elif(arr[m]>elem):
			l=m
		else:
			return m
	return -1
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



			
