import heapq

class MaxHeap:
    def __init__(self, l=None):
        self.pq = []
        if l:
            # Convertimos los elementos a sus valores negativos
            self.pq = [-x for x in l]
            heapq.heapify(self.pq)  # Convertimos la lista en un heap

    def push(self, element):
        # Insertamos el valor negativo para simular un max-heap
        heapq.heappush(self.pq, -element)

    def pop(self):
        # Extraemos el valor negativo y lo convertimos de nuevo a positivo
        return -heapq.heappop(self.pq)

    def peek(self):
        # Devolvemos el valor máximo (el negativo del valor mínimo en el heap)
        return -self.pq[0] if self.pq else None

    def empty(self):
        return not bool(self.pq)

    def __len__(self):
        return len(self.pq)

    def __str__(self):
        # Convertimos los valores negativos de nuevo a positivos para la representación
        return f"{[-x for x in self.pq]}"

class MinHeap:
	def __init__(self,l=None):
		self.pq=[]
		if(l):
			self.pq=l
			heapq.heapify(self.pq)
	def push(self,element):
		heapq.heappush(self.pq,element)
	def pop(self):
		return heapq.heappop(self.pq)
	def peek(self):
		return self.pq[0] if  self.pq else None
	def empty(self):
		return bool(self.pq)
	def __len__(self):
		return len(self.pq)
	def __str__(self):
		return f"{self.pq}"
####################################################
def find_k_smallest(arr,k):
	pq=MinHeap(arr)
	return [pq.pop() for _ in range(k)]
####################################################
def find_k_largest(arr,k):
	pq=MaxHeap(arr)
	return [pq.pop() for _ in range(k)]
####################################################



if __name__=="__main__":
	# Prueba
	arr = [3, 2, 1, 15, 5, 4, 45]
	k = 7
	print(f"Los {k} elementos más pequeños son:", find_k_smallest(arr, k))  # Salida: [1, 2, 3]
	pq=MaxHeap([5,34,1,4,33,2,3,3333])
	print(pq)
	pq.push(6)
	print(pq)
	print(len(pq))
	for i in range(len(pq)):	
 		print(pq.pop())
	

