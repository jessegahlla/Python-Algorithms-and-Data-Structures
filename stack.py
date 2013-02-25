class stack:
	def __init__ (self):
		self.container = []
	def isEmpty(self):
		return self.container == []
	def push(self, element):
		self.container.append(element)
	def pop(self):
		return self.container.pop()
	def peek(self):
		return self.container[len(self.container)-1]
	def size(self):
		return len(self.container)