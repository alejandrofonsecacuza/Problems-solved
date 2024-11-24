class stack:
	def __init__(self):
		self.s=[]
	def push(self,elem):
		self.s.append(elem)
	def top(self):
		assert self.s, "The stack is empty"
		return self.s[-1]
	def pop(self):
		assert self.s, "The stack is empty"
		self.s.pop()
	def __len__(self):
		return len(self.s)
	
s=stack()
s.push(10)
s.push(100)
s.pop()
s.pop()


		
		
