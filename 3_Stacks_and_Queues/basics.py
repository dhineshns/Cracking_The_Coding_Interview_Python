class Stack:
	def __init__(self):
		self.buff = []
	def push(self, value):
	 	self.buff.append(value)
	def pop(self):
	 	return self.buff.pop()
	def peek(self):
	 	return self.buff[-1]
	def __str__(self):
	 	return str(self.buff)
	def isEmpty(self):
		return (self.buff == [])

stackA = Stack()
for i in range (1, 20):
	stackA.push(i)

print stackA
print stackA.pop()
print stackA.peek()


	 		
