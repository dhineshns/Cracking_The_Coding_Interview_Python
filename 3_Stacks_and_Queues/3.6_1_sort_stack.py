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
def sort(input):
	output = Stack()
	while(not input.isEmpty()):
		tmp = input.pop()
		while (not output.isEmpty()  and (output.peek() < tmp)):
			input.push(output.pop())
		output.push(tmp)
	return output



input = Stack()
input.push(1)
input.push(5)
input.push(2)
input.push(10)
input.push(7)

print sort(input)
