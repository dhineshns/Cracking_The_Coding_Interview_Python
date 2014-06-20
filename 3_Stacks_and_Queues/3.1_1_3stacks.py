buff = [None]*15
top = [-1,-1,-1]
stackSize = 5
def push(value, stackNum):
	index = top[stackNum] + stackNum * stackSize + 1
	buff[index] = value
	top[stackNum]+=1
def pop(stackNum):
	index = top[stackNum] + stackNum * stackSize
	tmp = buff[index]
	buff[index] = None
	top[stackNum]-=1
	return tmp
def peek(stackNum):
	index = top[stackNum] + stackNum * stackSize
	return buff[index]
def display(stackNum):
	for i in range(stackNum*stackSize, stackNum*stackSize+stackSize):
		print buff[i]
push(1,0)
push(2,0)
push(3,0)
push(1,1)
push(2,1)
push(3,1)
push(1,2)
push(2,2)

display(0)
print "-----"
display(1)
print "-----"
display(2)
print "-----"

pop(1)
display(0)
print "-----"

print peek(1)

print "-----"