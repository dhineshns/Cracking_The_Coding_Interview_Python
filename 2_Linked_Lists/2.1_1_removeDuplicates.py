class Node:
	def __init__(self, contents, next = None):
		self.contents = contents
		self.next = next
class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
	def append(self, node):
		node = Node(node)
		if (self.head == None and self.tail == None) :
			self.head = node
			self.tail = node
		elif (self.tail) :
			self.tail.next = node
			self.tail = node		
	def printLL(self):
		node = self.head
		while(node):
			print node.contents
			node = node.next

def removeDuplicates(ll):
	node = ll.head
	output = LinkedList()
	checker = {}
	while(node):
		if not checker.has_key(node.contents):
			checker[node.contents] = True
			output.append(node.contents)
		node = node.next
	return output

ll = LinkedList()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(4)
ll.append(2)

output = removeDuplicates(ll)

output.printLL()