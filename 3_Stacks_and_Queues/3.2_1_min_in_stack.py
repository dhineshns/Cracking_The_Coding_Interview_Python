class Node:
	def __init__(self, contents, min = None, next = None):
		self.contents = contents
		self.min = min
		self.next = next
	def __str__(self):
		return str(self.contents)
class Stack:
	def __init__(self):
		self.buff = []
	def push(self, value):
		if (self.buff == []):
			value.min = value.contents
		else:
			value.next = self.buff[-1]
			if (value.contents < value.next.min):
				value.min = value.contents
			else:
				value.min = value.next.min
		self.buff.append(value)
		print  value.min

	def pop(self):
	 	return self.buff.pop()
	def peek(self):
	 	return self.buff[-1]
	def __str__(self):
	 	return str(self.buff)
	def isEmpty(self):
		return (self.buff == [])

stack = Stack()
stack.push(Node(10))
stack.push(Node(1))
stack.push(Node(10))
stack.push(Node(10))
stack.push(Node(11))

stack.push(Node(4))
stack.push(Node(1))
stack.push(Node(10))


print stack.peek().min