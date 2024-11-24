from collections import deque
#Deque es una lista doblemente enlazada

class queue:
	def __init__(self):
		self.q=deque()
	def enqueue(self,elem):
		self.q.append(elem)
	def dequeue(self):
		assert self.q, "The queue is empty"
		self.q.popleft(0)
	def __len__(self):
		return len(self.q)

		
