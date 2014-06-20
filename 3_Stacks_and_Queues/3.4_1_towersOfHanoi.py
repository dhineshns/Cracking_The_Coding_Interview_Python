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

def move(n, depart, dest, buff):
	if n==1:
		dest.push(depart.pop())
		return True
	if n>1:
		move(n-1, depart, buff, dest) 
		move(1, depart, dest, buff)
		move(n-1, buff, dest, depart)
		return True
n=5

stack1 = Stack()
stack2 = Stack()
stack3 = Stack()

for i in range(n,0, -1):
	stack1.push(i)

print stack1, stack2, stack3
move(n, stack1, stack3, stack2)

print stack1, stack2, stack3
