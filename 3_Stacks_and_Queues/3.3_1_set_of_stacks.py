class Stack:
	def __init__(self):
		self.buff = []
		self.size = 5
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
	def isFull(self):
		if (len(self.buff) < self.size):
			return False
		elif len(self.buff) >= self.size:
			return True
	def __str__(self):
		return str(self.buff)

class SetOfStacks:
	def __init__(self):
		stack = Stack()
		self.stackList = []
		self.stackList.append(stack)
	def push(self, value):
		last = self.getLastStack()
		if (not last.isFull()):
			last.push(value)
		else:
			self.addNewStack().push(value)
	def pop(self):
		last = self.getLastStack()
		if(not last.isEmpty()):
			return last.pop()
		else:
			return self.deleteEmptyStack().pop()
	def deleteEmptyStack(self):
		self.stackList.pop()
		return self.stackList[-1]
	def addNewStack(self):
		self.stackList.append(Stack())
		return self.stackList[-1]
	def __str__(self):
		for i in self.stackList:
			print i
		return "-----------"

	def getLastStack(self):
		return self.stackList[-1]

setOfstacks = SetOfStacks()
for i in range(1,17):
	setOfstacks.push(i)
print setOfstacks

setOfstacks.pop()
setOfstacks.pop()
print setOfstacks