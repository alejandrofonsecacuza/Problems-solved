import heapq

class priority_queue:
	def __init__(self,l=None):
		self.pq=[]
		if(l):
			self.pq=l
			heapq.heapify(self.pq)
		
	def insert(self,element):
		heapq.heappush(self.pq,element)
	def pop(self):
		return heapq.heappop(self.pq)
	def __len__(self):
		return len(self.pq)
	def __str__(self):
		aux=self.pq.copy()
		return f"{[heapq.heappop(aux) for _ in range(len(pq)) ]}"

pq=priority_queue([5,34,1,4,33,2,3,3333])
print(pq)
pq.insert(6)
print(pq)
print(len(pq))

