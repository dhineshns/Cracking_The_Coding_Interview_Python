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
	def length(self):
		return len(self.buff)
class MyQueue:
	def __init__(self):
		self.stack1 = Stack()
		self.stack2 = Stack()
	def push(self, value):
		self.stack2.push(value)
	def pop(self):
		if(self.stack1.isEmpty()):
			for i in range(0, self.stack2.length()):
				self.stack1.push(self.stack2.pop())
			return self.stack1.pop()
		else:
			return self.stack1.pop()
	def __str__(self):
		print self.stack1
		print self.stack2
		return "---------"


myQ = MyQueue()

for i in range(1, 10):
	myQ.push(i)

print myQ

myQ.pop()
print myQ