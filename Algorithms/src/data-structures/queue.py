class queue:
	def __init__(self):
		self.q=[]
	def push(self,elem):
		self.q.append(elem)
	def pop(self):
		assert self.q, "The queue is empty"
		self.q.pop(0)
	def __len__(self):
		return len(self.q)

		
